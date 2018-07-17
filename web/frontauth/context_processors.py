
def front_user(request):
	if hasattr(request,'frontuser'):
		frontuser = request.frontuser
		return {
			'frontuser': frontuser
		}
	else:
		return {
			'frontuser': None
		}

