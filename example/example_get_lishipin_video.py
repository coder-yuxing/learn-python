import requests


def download_video(page_url: str) -> None:
    # 从路径中获取视频ID
    cont_id = page_url.split('_')[1]
    video_api = f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}' \
                f'&mrd=0.29878533327525947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                      'Safari/537.36',
        # HTTP Referer是header的一部分，当浏览器向web服务器发送请求的时候，
        # 一般会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器 籍此可以获得一些信息用于处理
        'Referer': page_url
    }
    # 请求api 获取视频资源
    resp = requests.get(video_api, headers=headers)
    data = resp.json()
    system_time = data['systemTime']
    video_src_url = data['videoInfo']['videos']['srcUrl']
    # 获取真实的视频访问地址
    src_url = video_src_url.replace(system_time, f'cont-{cont_id}')

    # 下载视频
    with open(f'temp/{cont_id}.mp4', mode='wb') as f:
        f.write(requests.get(src_url).content)


if __name__ == '__main__':
    video_source_url = 'https://www.pearvideo.com/video_1763204'
    download_video(video_source_url)
