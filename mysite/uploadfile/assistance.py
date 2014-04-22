from mysite.settings import DOUCMENT_ROOT



def handle_uploaded_file(f):
    name = "%s" % f.name
    destination = open('%s/%s' % (DOUCMENT_ROOT, name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()