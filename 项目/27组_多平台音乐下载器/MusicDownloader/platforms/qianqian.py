'''
Function:
	千千音乐下载: http://music.taihe.com/
'''
import os
import click
import requests
from contextlib import closing

class qianqian():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
						'referer': 'http://music.taihe.com/'
						}
		self.search_url = "http://musicapi.qianqian.com/v1/restserver/ting"
		self.player_url = 'http://music.baidu.com/data/music/links'
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
					songid = self.search_results.get(download_name)
					params = {"songIds": songid}
					res = requests.get(self.player_url, params=params, headers=self.headers)
					if not res.json().get('data').get('songList'):
						continue
					download_url = res.json().get('data').get('songList')[0].get('songLink')
					if not download_url:
						continue
					res = self.__download(download_name, download_url, savepath, '.mp3')
					if res:
						downed_list.append(download_name)
			return downed_list
		else:
			raise ValueError('mode in qianqian().get must be <search> or <download>...')
	'''下载'''
	def __download(self, download_name, download_url, savepath, extension):
		if not os.path.exists(savepath):
			os.mkdir(savepath)
		download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
									 .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
									 .replace('|', '').replace('？', '').replace('*', '')
		savename = '千千音乐_{}'.format(download_name)
		count = 0
		while os.path.isfile(os.path.join(savepath, savename+extension)):
			count += 1
			savename = '千千音乐_{}_{}'.format(download_name, count)
		savename += extension
		try:
			print('[千千]: 正在下载 --> %s' % savename.split('.')[0])
			with closing(requests.get(download_url, headers=self.headers, stream=True, verify=False)) as res:
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
		params = {
				"query": songname,
				"method": "baidu.ting.search.common",
				"format": "json",
				"page_no": 1,
				"page_size": 15
				}
		res = requests.get(self.search_url, params=params, headers=self.headers)
		results = {}
		for song in res.json()['song_list']:
			songid = song.get('song_id')
			singers = song.get('author')
			album = song.get('album_title')
			download_name = '%s--%s--%s' % ( song.get('title').replace("<em>", "").replace("</em>", ""), singers, album)
			count = 0
			while download_name in results:
				count += 1
				download_name = '%s(%d)--%s--%s' % (song.get('title'), count, singers, album)
			results[download_name] = songid
		return results
