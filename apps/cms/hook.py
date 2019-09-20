from .views import bp
from .models import CMSPersmission

@bp.context_processor  #上下文处理器, 返回的字典可以在全部模板中使用
def context_processor():
    return {'CMSPersmission':CMSPersmission}


