'''
Function:
	酷狗音乐下载: http://www.kugou.com/
'''
import re
import os
import time
import click
import requests
from contextlib import closing

class kugou():
	def __init__(self):
		self.headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
					}
		self.down_headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
					'Host': 'webfs.yun.kugou.com',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive'
					}
		self.search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30'
		self.hash_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}&dfid=&mid=ccbb9592c3177be2f3977ff292e0f145&platid=4'
		self.search_results = {}
	'''外部调用'''
	def get(self, mode='search', **kwargs):
		if mode == 'search':
			songname = kwargs.get('songname')
			self.search_results = self.__searchBySongname(songname)
			return self.search_results
		elif mode == 'download':
			need_down_list = kwargs.get('need_down_list')
			downed_list = []
			savepath = kwargs.get('savepath') if kwargs.get('savepath') is not None else './downloads'
			if need_down_list is not None:
				for download_name in need_down_list:
					filehash, album_id = self.search_results.get(download_name)
					res = requests.get(self.hash_url.format(filehash, album_id))
					play_url = re.findall('"play_url":"(.*?)"', res.text)[0]
					download_url = play_url.replace("\\", "")
					if not download_url:
						continue
					res = self.__download(download_name, download_url, savepath, '.mp3')
					if res:
						downed_list.append(download_name)
			return downed_list
		else:
			raise ValueError('mode in kugou().get must be <search> or <download>...')
	'''下载'''
	def __download(self, download_name, download_url, savepath, extension='.mp3'):
		if not os.path.exists(savepath):
			os.mkdir(savepath)
		download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
									 .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
									 .replace('|', '').replace('？', '').replace('*', '')
		savename = '酷狗音乐_{}'.format(download_name)
		count = 0
		while os.path.isfile(os.path.join(savepath, savename+extension)):
			count += 1
			savename = '酷狗音乐_{}_{}'.format(download_name, count)
		savename += extension
		try:
			print('[酷狗]: 正在下载 --> %s' % savename.split('.')[0])
			with closing(requests.get(download_url, headers=self.down_headers, stream=True, verify=False)) as res:
				total_size = int(res.headers['content-length'])
				if res.status_code == 200:
					label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
					with click.progressbar(length=total_size, label=label) as progressbar:
						with open(os.path.join(savepath, savename), "wb") as f:
							for chunk in res.iter_content(chunk_size=1024):
								if chunk:
									f.write(chunk)
									progressbar.update(1024)
				else:
					raise RuntimeError('Connect error...')
			return True
		except:
			return False
	'''根据歌名搜索'''
	def __searchBySongname(self, songname):
		res = requests.get(self.search_url.format(songname), headers=self.headers)
		results = {}
		for song in res.json()['data']['lists']:
			filehash = song.get('FileHash')
			singers = song.get('SingerName')
			album = song.get('AlbumName')
			album_id = song.get('AlbumID')
			download_name = '%s--%s--%s' % (song.get('SongName'), singers, album)
			count = 0
			while download_name in results:
				count += 1
				download_name = '%s(%d)--%s--%s' % (song.get('SongName'), count, singers, album)
			results[download_name] = [filehash, album_id]
		return results

