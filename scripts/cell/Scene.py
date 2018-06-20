# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Scene(KBEngine.Entity):
	"""
	Scene的cell部分。cell上一个space代表的是一个抽象的空间，该Scene是该抽象空间的实体呈现，方便进行控制
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		# 存储在globalData中，方便获取
		KBEngine.globalData["scene"] = self.base
		
	def onEnter(self, entityCall):
		"""
		defined method.
		进入场景
		"""
		DEBUG_MSG('Scene[%i]::onEnter: entityID = %i.' % (self.id, entityCall.id))

	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		DEBUG_MSG('Scene[%i]::onLeave: entityID = %i.' % (self.id, entityID))

	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁时被调用
		"""
		del KBEngine.globalData["scene"]
		# api：销毁scene实体所在的空间
		self.destroySpace()
