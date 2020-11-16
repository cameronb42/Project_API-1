import requests

HOST = "http://34.121.122.205"

#For test calculations
all_tests = 0
correct_tests = 0


#Testing dictionaries of each endpoint
md5_tester = {
    "test": "098f6bcd4621d373cade4e832627b4f6",
    "testtesttest": "1fb0e331c05a52d5eb847d6fc018320d",
    "tester": "f5d1278e8109edd94e1e4197e04873b9"
}
keyval_tester = {
    "foo": "bar",
    "hello": "world",
    "test": "test3"
}
prime_tester = {
    8: False,
    6: False,
    2: True
}
factorial_tester = {
    4: 24,
    5: 120,
    9: 362880
}
fibonacci_tester = {
    56: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    18: [0, 1, 1, 2, 3, 5, 8, 13],
    10: [0, 1, 1, 2, 3, 5, 8]
}


#Starting keyval testing with for loops and response codes
for a in keyval_tester.keys():
    all_tests += 1
    r = requests.post(HOST + "/keyval/" + str(a) + "/" + str(keyval_tester[a]))
    if r.status_code == 200:
        correct_tests += 1
        print("Test POST Passed!")
    else:
        print("Test POST Failed- response code ", str(r.status_code))

for a in keyval_tester.keys():
    all_tests += 1
    r = requests.get(HOST + "/keyval/" + str(a))
    right = keyval_tester[a]
    if r.status_code == 200:
        v = r.json()["value"]
        if v == str(right):
            correct_tests += 1
            print("Test GET Passed!")
        else:
            print("Test GET Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test GET Failed- response code ", str(r.status_code))

for a in keyval_tester.keys():
    all_tests += 1
    r = requests.delete(HOST + "/keyval/" + str(a))
    if r.status_code == 200:
        correct_tests += 1
        print("Test DELETE Passed!")
    else:
        print("Test DELETE Failed- response code ", str(r.status_code))


#Starting md5 testing 
for a in md5_tester.keys():
    all_tests += 1
    r = requests.get(HOST + "/md5/" + str(a))
    right = md5_tester[a]
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test md5 Passed!")
        else:
            print("Test md5 Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test md5 Failed- response code ", str(r.status_code))


#Starting prime testing
for a in prime_tester.keys():
    all_tests += 1
    r = requests.get(HOST + "/is-prime/" + str(a))
    right = prime_tester[a]
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Prime Passed!")
        else:
            print("Test Prime Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Prime Failed- response code ", str(r.status_code))


#Starting factorial testing
for a in factorial_tester.keys():
    all_tests += 1
    r = requests.get(HOST + "/factorial/" + str(a))
    right = factorial_tester[a]
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Factorial Passed!")
        else:
            print("Test Factorial Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Factorial Failed- response code ", str(r.status_code))


#Starting fibonacci sequence testing
for a in fibonacci_tester.keys():
    all_tests += 1
    r = requests.get(HOST + "/fibonacci/" + str(a))
    right = fibonacci_tester[a]
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Fibonacci Passed!")
        else:
            print("Test Fibonacci Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Fibonacci Failed- response code ", str(r.status_code))


#Starting slack-alert testing
all_tests += 1
r1 = requests.get(HOST + "/slack-alert/Hello.")
all_tests += 1
r2 = requests.get(HOST + "/slack-alert/This%20Is%20A%20Longer%20String")
if r1.status_code == 200 and r2.status_code == 200:
    print("Test Slack-alert Passed! Both messages posted.")
    correct_tests += 2
else:
    if r1.status_code != 200:
        print("'Hello.' could not post to channel- response code: ", str(r1.status_code))
    else:
        correct_tests += 1

    if r2.status_code != 200:
        print("'This Is A Longer String' could not post to channel- response code: ", str(r2.status_code))
    else:
        correct_tests += 1
    print("Test Slack-alert Failed!")


#Final test calculations of all tests
print("\nCorrect tests: ", str(correct_tests))
print("All tests: ", str(all_tests))
print("Total score: ", str((correct_tests / all_tests)*100))
