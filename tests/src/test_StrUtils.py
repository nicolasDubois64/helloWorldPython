from helloWorldPython.src.features.StrUtils import myConcat
from helloWorldPython.src.features.StrUtils import functionThatCallsMyConcat
from helloWorldPython.src.features.StrUtils import getIsLeapYearMsg
from helloWorldPython.src.features.StrUtils import uniformize

def test_myConcat():
    """
    Simplest possible test example
    """
    assert myConcat("bon","jour") == "bonjour"

def test_myConcatDefaultValue():
    assert myConcat("grosse") == "grossebiere"

def test_functionThatCallsMyConcat(mocker):
    """
    Example with a mock fonction
    See more => https://changhsinlee.com/pytest-mock/
    """
    expectedResult = "bonjour!"
    mockValue = "bonjour"
    mocker.patch('helloWorldPython.src.features.StrUtils.myConcat', return_value = mockValue)
    actualResult = functionThatCallsMyConcat("bon", "jour")
    assert expectedResult == actualResult

def test_getIsLeapYearMsg(mocker):
    """
    Example of a mock of an imported function
    """
    expectedResult = "2019 est bien une année bissextile!"
    mockValue = True
    # isLeapYear is from DateUtils.py but imported to StrUtils.py
    mocker.patch('helloWorldPython.src.features.StrUtils.isLeapYear', return_value = mockValue)
    actualResult = getIsLeapYearMsg(2019)
    assert expectedResult == actualResult

def test_uniformize():
    inputData="BON(JOUR)."
    expectedResult = "bonjour"
    assert uniformize(inputData) == expectedResult