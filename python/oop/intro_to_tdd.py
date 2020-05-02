import unittest

def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i] 
    return list

class reverseListTest(unittest.TestCase):
    def testOneR(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
    def testTwoR(self):
        self.assertEqual(reverseList([5,3,6,1]),[1,6,3,5])
    def testThreeR(self):
        self.assertEqual(reverseList([4,3,2,1]), [1,2,3,4])
    def testFourR(self):
        self.assertEqual(reverseList([18,19]), [19,18])
    def testFiveR(self):
        self.assertEqual(reverseList([3,2,1]), [1,2,3])
    def testSixR(self):
        self.assertEqual(reverseList([6,9]), [9,6])

def isPalindrome(str): 
    for i in range(int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True

class isPalindromeTest(unittest.TestCase):
    def testOneP(self):
        self.assertEqual(isPalindrome("racecar"), True ) 
    def testTwoP(self):
        self.assertFalse(isPalindrome("rabcr") )
    def testThreeP(self):
        self.assertEqual(isPalindrome("civic"), True )
    def testFourP(self):
        self.assertFalse(isPalindrome("tree") )
    def testFiveP(self):
        self.assertEqual(isPalindrome("noon"), True )
    def testSixP(self):
        self.assertFalse(isPalindrome("house"))

def coin(c):
    res = []
    res.append(int(c / 25))
    c -= 25* res[0]
    res.append(int(c / 10))
    c -= 10 * res[1]
    res.append(int(c / 5))
    c -= 5 * res[2]
    res.append(int(c / 1))
    c -= 1 * res[3]
    return res

class coins(unittest.TestCase):
    def testOneC(self):
        self.assertEqual( coin(87), [3,1,0,2] )
    def testTwoC(self):
        self.assertEqual( coin(85), [3,1,0,0] )
    def testThreeC(self):
        self.assertEqual( coin(80), [3,0,1,0] )
    def testFourC(self):
        self.assertEqual( coin(75), [3,0,0,0] )
    def testFiveC(self):
        self.assertEqual( coin(50), [2,0,0,0] )

if __name__ == '__main__':
    unittest.main()