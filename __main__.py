

from simplemdx.set import set
from simplemdx.member import member

mdx = set('account').members(['test', 'cats', 'morton']).to_mdx()

print(mdx)

