'''
Function:
	酷我音乐下载: http://yinyue.kuwo.cn/
'''
import re
import os
import click
import requests
from contextlib import closing

class kuwo():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' 
						}
		self.search_url = 'http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku2016&key={}'
		self.player_url = 'http://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid=MUSIC_{}'
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
					res = requests.get(self.player_url.format(songid), headers=self.headers)
					mp3dl = re.findall(r'<mp3dl>(.*?)</mp3dl>', res.text)[0]
					mp3path = re.findall(r'<mp3path>(.*?)</mp3path>', res.text)[0]
					download_url = 'http://' + mp3dl + '/resource/' + mp3path
					res = self.__download(download_name, download_url, savepath, '.mp3')
					if res:
						downed_list.append(download_name)
			return downed_list
		else:
			raise ValueError('mode in kuwo().get must be <search> or <download>...')
	'''下载'''
	def __download(self, download_name, download_url, savepath, extension='.mp3'):
		if not os.path.exists(savepath):
			os.mkdir(savepath)
		download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
									 .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
									 .replace('|', '').replace('？', '').replace('*', '')
		savename = '酷我_{}'.format(download_name)
		count = 0
		while os.path.isfile(os.path.join(savepath, savename+extension)):
			count += 1
			savename = '酷我_{}_{}'.format(download_name, count)
		savename += extension
		try:
			print('[酷我-INFO]: 正在下载 --> %s' % savename.split('.')[0])
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
		res = requests.get(self.search_url.format(songname), headers=self.headers)
		infos = re.findall(r'<a href="http://www\.kuwo\.cn/yinyue/(.*?)/" title="(.*?)" target="_blank">', res.text)
		albums = re.findall(r'\<p class="a_name"\>(.*?)\</p\>', res.text)
		all_singers = re.findall(r'\<p class="s_name"\>(.*?)\</p\>', res.text)
		results = {}
		for i in range(len(infos)):
			songid = infos[i][0]
			singers = re.findall(r'title="(.*?)"', all_singers[i])
			singers = ','.join(singers)
			try:
				album = re.findall(r'title="(.*?)"', albums[i])[0]
			except:
				album = '无专辑'
			download_name = '%s--%s--%s' % (infos[i][1], singers, album)
			count = 0
			while download_name in results:
				count += 1
				download_name = '%s(%d)--%s--%s' % (infos[i][1], count, singers, album)
			results[download_name] = songid
		return results

