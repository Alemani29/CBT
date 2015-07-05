class player():
    motxilla = {'pinya':0, 'pinyapelada':0, 'poma':poma, 
    'money':money, 'ganivet':False}
    

    status = {'ganivetma':False}
    
    zona_incial = 'bosc'
    
    def showMotxilla(self):
        for key,value in self.motxilla.items() :
            if value==False:
                print(key,': ', 'no en tens')
            else:    
                print(key,': ', value)


class zona():
    id = 0
    accions = []
    llocs = []