from flask import Blueprint,make_response,render_template,make_response
from flask_restful import Resource,fields,marshal_with,Api

FIELDS_STRING_ = {
    # attribute 的意思是修改名称   把title修改成school
    "username": fields.String,
    "email": fields.String,

}

'''
使用ajax给前端进行传值

'''
#使用蓝图
blue_bp = Blueprint("blue",__name__,url_prefix="/blue")

#使用蓝图初始化app
api = Api(blue_bp)

class ArticleView(Resource):
    # 验证要传递的数据
    resource_fields = FIELDS_STRING_


    @marshal_with(resource_fields)
    def get(self,blue_id):
        #拿数据
        from exam import User
        article = User.query.get(blue_id)
        #传递数据
        print("----------",article)
        return article

api.add_resource(ArticleView,"/<blue_id>/",endpoint = "blue")