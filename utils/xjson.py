from flask import jsonify

class StatusCode(object):
    ok = 200            #成功
    paramserror = 400   #参数错误
    unauth = 401        #验证不通过
    methoderror = 405   #方法错误
    servererror = 500   #服务器内部错误

def json_result(code,message,data):
    return jsonify({"code":code,"message":message,"data":data or {}})

def json_sucess(message='',data=None):
    return json_result(code=StatusCode.ok,message=message,data=data)

def json_params_error(message='',data=None):
    """
    请求参数错误
    """
    return json_result(code=StatusCode.paramserror,message=message,data=data)

def json_unauth_error(message='',data=None):
    """
    没有权限访问
    """
    return json_result(code=StatusCode.unauth,message=message,data=data)


def json_method_error(message='',data=None):
    """
    请求方法错误
    """
    return json_result(code=StatusCode.methoderror,message=message,data=data)


def json_server_error(message='',data=None):
    '''
    服务器内部错误
    '''
    return json_result(code=StatusCode.servererror,message=message,data=data)


























