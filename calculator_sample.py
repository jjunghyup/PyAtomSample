# PyAtom Library import
import atomacos
# 계산기 어플을 bundle id를 통해서 실행하
atomacos.launchAppByBundleId('com.apple.calculator')

# 실행된 계산기 어플 Bundle id를 통해서 찾고 객체화하기
calculator = atomacos.getAppRefByBundleId('com.apple.calculator')

try:
    # 만약 계산기 앱이 정상수행되지 않을 경우 AXTitle 값이 객체에 없게 된다.
    getattr(calculator, 'AXTitle')
except:
    # 이럴경우 Exception이 발생하는데 발생하면 3초를 대기한 후 다음동작을 수행하도록 한다.
    import time
    time.sleep(3)
    calculator = atomacos.getAppRefByBundleId('com.apple.calculator')

# 정상적으로 객체 정보가 반영되었는지 확인
print(calculator)

# AXRole이 AXButton이고 AXTitle이 1인 값 찾기
one_button = calculator.findFirstR(AXRole='AXButton', AXTitle='1')
# 1버튼 속성값 확인하기
print(one_button.getActions())
# 1버튼 클릭하기
one_button.Press()

