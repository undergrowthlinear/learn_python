import requests as req


# 响应
def dis_rep(git_url):
    print(git_url, git_url, git_url)
    res = req.get(git_public_events)
    print(res.url, res.status_code, res.status_code == req.codes.ok,
          res.encoding)
    for k in res.headers:
        print(k, ':', res.headers[k])
    # print('显示响应内容')
    content_json = res.json()
    for t in content_json:
        print(t)
    print(git_url, git_url, git_url)

'''
 Request 对象
 Response 对象
'''
base_url = 'https://api.github.com'
git_public_events = base_url + '/events'
dis_rep(git_public_events)
#
'''
git_public_events = base_url + '/networks/XX-net/XX-Net/events'
dis_rep(git_public_events)
'''
# json转换
# print(json.dumps(content_json))
