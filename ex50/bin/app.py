import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        moonshine = "Ole Smokey Tennessee"
        #greeting = "Hey"
        #return render.index(greeting = greeting)
        return render.foo(moonshine = moonshine)


if __name__ == "__main__":
    app.run()
