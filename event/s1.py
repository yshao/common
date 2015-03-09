import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print "Doing stuff..."
    # do your stuff
    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()


def status_check(d):
    print "Doing stuff..."


def check_smap_backend():
    cfg=Env.getConfig()
    sub=(cfg['smap_server_ip'],cfg['smap_server_port'])
    ### curl on server
    r = requests.get('http://%(ip)s:%(port)s/api/query/Properties__UnitofMeasure' %sub)
    # print r.status_code
    if r.status_code == 200:
        print 'smap backend pass'
    else:
        print "smap backend failed"