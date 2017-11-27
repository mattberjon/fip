
def test_get_key(fip):
    fip.data = {'title': 'a title', 'authors': 'one author'}
    assert fip.get_key('title') == 'a title'
    assert fip.get_key('string') is None
