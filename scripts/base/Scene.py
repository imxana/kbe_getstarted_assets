# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Scene(KBEngine.Proxy):
	"""
	Scene的base部分，
	注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		# 向cellappmgr请求创建一个cell，并关联本实体对象
		# 参数cellappIndex为None，表示由引擎负载均衡进行动态选择
		self.createCellEntityInNewSpace(None)
		
	def onGetCell(self):
		"""
		entity的cell部分被创建成功
		"""
		props = {
			"name": "MyFirstEntity"
		}
		entity = KBEngine.createEntityLocally("FirstEntity", props)
		self.loginToScene(entity)
		
	def loginToScene(self, entityCall):
		"""
		某个Entity请求登录到该场景
		:param entityCall: 要进入本场景的实体entityCall
		"""
		entityCall.createCell(self.cell)
		# 通知scene的cell部分，有人进来了
		if self.cell is not None:
			self.cell.onEnter(entityCall)
			
	def logoutScene(self, entityId):
		"""
		某个玩家请求登出该场景
		:param entityId: 登出者的id
		"""
		# 通知scene的cell部分，有人离开了
		if self.cell is not None:
			self.cell.onLeave(entityId)