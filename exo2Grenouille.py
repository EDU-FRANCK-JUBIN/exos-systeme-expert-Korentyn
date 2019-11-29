from pyDatalog import pyDatalog
# ajout des règles
pyDatalog.load("""
    frog(X) <= croakes(X) & eatsFlies(X)
    canary(X) <= chirps(X) & sings(X)
    green(X) <= frog(X)
    yellow(X) <= canary(X)
""")

pyDatalog.assert_fact('croakes', 'fritz')
pyDatalog.assert_fact('eatsFlies', 'fritz')

print(pyDatalog.ask('green(X)'))
