class ValidationError(Exception):
    pass
class DuplicateUserError(Exception):
    pass
user_name=[]
def  validate_username(username):
    if len(username) < 3:
        raise ValidationError(f'用户名必须包含3个字符,当前{len(username)}个')
    if not username.isalnum():
        raise ValidationError('用户名只能包含字母和数字')
    if username in user_name:
        raise DuplicateUserError('用户名已被占用')
    return username
def validate_age(age_text):
    try:
        age =int(age_text)
    except ValueError:
        raise ValidationError('年龄必须为数字')
    if not (0 <=age<= 150):
        raise ValidationError("年龄范围为0到150之间")
    return age
def validate_password(password):
    if len(password)<6:
        raise ValidationError('密码至少6位')
    if not password.isalnum():
        raise ValidationError('用户名只能包含字母和数字')
    return password
def input_with_retry(prompt,validator,max_retry=3):
    for attempt in range(1,max_retry+1):
        try:
            value=input(prompt)
            result=(validator(value))
        except ValidationError as e:
            print(f'❌第{attempt}/{max_retry}次:{e}')
        else:
            return result
    raise ValidationError(f'连续输入{max_retry}次错误，结束输入')


while True:
    try:
        username=input_with_retry('请用户输入姓名: ',validate_username,4)
        age=input_with_retry('请用户输入年龄: ',validate_age,5)
        password=input_with_retry('请用户输入密码: ',validate_password,6)
    except ValidationError as e:
        print('用户注册失败')
    else:
        print(f'✅注册成功，用户{username},{age}岁')
        user_name.append(username)
    finally:
        print('感谢使用注册系统')





