# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Account(KBEngine.Proxy):
	def __init__(self):
		"""
		账号实体
		客户端登陆到服务端后，服务端将自动创建这个实体，通过这个实体与客户端进行账户相关交互
		"""
		KBEngine.Proxy.__init__(self)
		
	def createCell(self, sceneCell):
		"""
		创建cell部分
		:param sceneCell:场景的cellEntityCall
		"""
		# API：创建该实体的cell部分
		self.createCellEntity(sceneCell)

	def enterGame(self):
        """
        客户端点击进入游戏按钮后发来的请求
        :return:
        """
        self.client.onEnterGameSuccess()
        # 把自己传送到指定的scene
        KBEngine.globalData["scene"].loginToScene(self)

	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()
