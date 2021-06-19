# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from enum import Enum

class ResultCodeEnum(Enum):
    SUCCESS = (200, "成功")
    FAIL = (201, "失败")
    PARAM_ERROR = (202, "参数不正确")
    SERVICE_ERROR = (203, "服务异常")
    DATA_ERROR = (204, "数据异常"),

    URL_NOT_FOUND = (216, "URL找不到")
    FETCH_USERINFO_ERROR = (220, "获取用户信息失败")

    LOGIN_AUTH = (508, "未登陆")
    PERMISSION = (509, "没有权限")

    CODE_ERROR = (510, "验证码错误")
    LOGIN_DISABLED_ERROR = (512, "该用户已被禁用")
    REGISTER_USERNAME_ERROR = (514, "用户名已被使用")
    LOGIN_USER_FAIL = (517, "用户名或密码错误")

    """根据code获取描述"""
    @staticmethod
    def getDescribeByCode(code:int) -> None:
        for item in ResultCodeEnum:
            if item.value[0] == code:
                return item.value[1]
