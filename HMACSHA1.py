#!/usr/bin/python

import hmac
import base64

#其中StringToSign需要替换为对应的内容。
message = b'POST&%2F&AccessKeyId%3Dtestid&AccountName%3D%253Ca%2525b%2527%253E&Action%3DSingleSendMail&AddressType%3D1&Format%3DXML&HtmlBody%3D4&RegionId%3Dcn-hangzhou&ReplyToAddress%3Dtrue&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3Dc1b2c332-4cfb-4a0f-b8cc-ebe622aa0a5c&SignatureVersion%3D1.0&Subject%3D3&TagName%3D2&Timestamp%3D2016-10-20T06%253A27%253A56Z&ToAddress%3D1%2540test.com&Version%3D2015-11-23'
key = b'testsecret&'
h = hmac.new(key, message, digestmod='sha1')
print(h.digest())

print(base64.b64encode(h.digest()))
