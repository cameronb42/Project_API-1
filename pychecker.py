import requests

HOST = "http://34.121.122.205"

#Testing dictionaries of each endpoint
keyval_tests = {
    "foo": "bar",
    "hello": "world",
    "test": "test3"
}

md5_tests = {
    "test": "098f6bcd4621d373cade4e832627b4f6",
    "testtesttest": "1fb0e331c05a52d5eb847d6fc018320d",
    "tester": "f5d1278e8109edd94e1e4197e04873b9"
}

prime_tests = {
    8: False,
    6: False,
    2: True
}

fibonacci_tests = {
    56: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    18: [0, 1, 1, 2, 3, 5, 8, 13],
    10: [0, 1, 1, 2, 3, 5, 8]
}

factorial_tests = {
    4: 24,
    5: 120,
    9: 362880
}


#For test calculations
all_tests = 0
correct_tests = 0


#Starting keyval testing with for loops and response codes
print("\t\tLaunching keyval tests!")
for a in keyval_tests.keys():
    all_tests += 1
    r = requests.post(HOST + "/keyval/" + str(a) + "/" + str(keyval_tests[a]))
    print("Post Key: ", str(a), " to ", str(keyval_tests[a]))
    if r.status_code == 200:
        correct_tests += 1
        print("Test Passed!")
    else:
        print("Test Failed- response code ", str(r.status_code))

for a in keyval_tests.keys():
    all_tests += 1
    r = requests.get(HOST + "/keyval/" + str(a))
    right = keyval_tests[a]
    print("Get Key: ", str(a), ", anticipating ", str(right))
    if r.status_code == 200:
        v = r.json()["value"]
        if v == str(right):
            correct_tests += 1
            print("Test Passed!")
        else:
            print("Test Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Failed- response code ", str(r.status_code))

for a in keyval_tests.keys():
    all_tests += 1
    r = requests.delete(HOST + "/keyval/" + str(a))
    print("Delete Key: ", str(a))
    if r.status_code == 200:
        correct_tests += 1
        print("Test Passed!")
    else:
        print("Test Failed- response code ", str(r.status_code))


#Starting md5 testing 
print("\t\tLaunching md5 tests!")
for a in md5_tests.keys():
    all_tests += 1
    r = requests.get(HOST + "/md5/" + str(a))
    right = md5_tests[a]
    print("Value is ", str(a), ", anticipating ", str(right))
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Passed!")
        else:
            print("Test Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Failed- response code ", str(r.status_code))


#Starting prime testing
print("\t\tLaunching prime tests!")
for a in prime_tests.keys():
    all_tests += 1
    r = requests.get(HOST + "/is-prime/" + str(a))
    right = prime_tests[a]
    print("Prime of ", str(a), ", expecting ", str(right))
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Passed!")
        else:
            print("Test Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Failed- response code ", str(r.status_code))


#Starting factorial testing
print("\t\tLaunching factorial tests!")
for a in factorial_tests.keys():
    all_tests += 1
    r = requests.get(HOST + "/factorial/" + str(a))
    right = factorial_tests[a]
    print("Factorial of ", str(a), ", expecting ", str(right))
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Passed!")
        else:
            print("Test Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Failed- response code ", str(r.status_code))


#Starting fibonacci sequence testing
print("\t\tLaunching fibonacci tests!")
for a in fibonacci_tests.keys():
    all_tests += 1
    r = requests.get(HOST + "/fibonacci/" + str(a))
    right = fibonacci_tests[a]
    print("Fibonacci sequence until ", str(a), ", anticipating ", str(right))
    if r.status_code == 200:
        v = r.json()["output"]
        if v == right:
            correct_tests += 1
            print("Test Passed!")
        else:
            print("Test Failed- retrieved this value ", str(v), " instead of ", str(right))
    else:
        print("Test Failed- response code ", str(r.status_code))


#Starting slack-alert testing
print("\t\tLaunching slack tests!")
all_tests += 1
r1 = requests.get(HOST + "/slack-alert/Hello.")
all_tests += 1
r2 = requests.get(HOST + "/slack-alert/This%20Is%20A%20Longer%20String")
if r1.status_code == 200 and r2.status_code == 200:
    print("Test Passed! Both messages posted.")
    correct_tests += 2
else:
    if r1.status_code != 200:
        print("Message 'Hello.' could not post to channel- response code: ", str(r1.status_code))
    else:
        correct_tests += 1

    if r2.status_code != 200:
        print("\nMessage 'This Is A Longer String' could not post to channel- response code: ", str(r2.status_code))
    else:
        correct_tests += 1
    print("Test Failed!")


#Final test calculations of all tests
print("\nCorrect tests: ", str(correct_tests))
print("All tests: ", str(all_tests))
print("Total: ", str((correct_tests / all_tests)*100))
