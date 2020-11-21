import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#from nose.tools import assert_true
import requests
from subprocess import check_output
import subprocess


def GitHash(gitrepoName):
    hash = check_output(["git", "ls-remote","-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    hashHead = hashHead[3:42]
    return hashHead
gitrepo = "https://github.com/michelescarlato/HelloEndoWorld.git"
GitHeadHash= GitHash(gitrepo)

def test_request_response():
    response = requests.get('http://0.0.0.0:7933/helloworld')
    assert response.status_code == 200
    res=response.text
    assert res == "Hello Stranger"
    #assert response.assertEqual("Hello Stranger")

def test_request_responseHelloName():
    response = requests.get('http://0.0.0.0:7933/helloworld/PaoloDeLuca')
    assert response.status_code == 200
    #assert response.assertEqual("Hello Stranger")
    res=response.text
    assert res == "Hello Paolo De Luca"

def test_request_responseJSON():
    response = requests.get('http://0.0.0.0:7933/versionz')
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["GitProject"] == "HelloEndoWorld"
    assert response_body["GitHeadHash"] == GitHeadHash
