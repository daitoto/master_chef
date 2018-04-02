响应：
	input：
		菜名*， isnew, userID, 询问类型(0:new, 1:next, 2:repeat)*
	output:
		文字，[音频], shouldEndSession

正则表达式:
	input:
		uttrance
	output:
		菜名， 询问类型

http read:
	input:
		json
	output:
		isnew, userID, uttrance*

http response:
	input:
		version, requestID, 文字, [音频], shouldEndSession
	output:
		json

http read-> 正则表达式-> 响应-> http response
