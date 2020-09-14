from pycipher import Bifid

ciphertext = 'snbwmuotwodwvcywfgmruotoozaiwghlabvuzmfobhtywftopmtawyhifqgtsiowetrksrzgrztkfctxnrswnhxshylyehtatssukfvsnztyzlopsv'
keys = ['mrocktvquizphdbagsfewlynx', 'ocknymphswaqfdrugvexblitz',
'crwthvoxzapsqigymfeldbunk', 'hmfordwaltzcinqbuskpyxveg',
'phavfyxbugstonqmilkzdcrew', 'hesaidbcfgklmnopqrtuvwxyz',
'enqvahlbidgumkrwcfpostxyz', 'emilyqungschwarzkopfxtvbd',
'ohnfezcamrwsputyxigkqblvd', 'qtipforsuvnzxylemdcbaghwk',
'umblingvextfrowzyhackspdq', 'qvandzstruckmybigfoxwhelp',
'lumpydrabcgqvzinksfoxthew', 'heyiamnopqrstuvwxzbcdfgkl',
'quizvbmwlynxstockderpaghf', 'pledbigczarunksmyvwfoxthq',
'waltzgbquickfordsvexnymph', 'qwertyuioplkhgfdsazxcvbnm',
'zyxwvutsrqponmlkihgfedcba', 'aquickbrownfxmpsvethlzydg',
]

for key in keys[::-1]:
    ciphertext = Bifid(key, 5).decipher(ciphertext)

    # Fill in the x
    print(str.lower(ciphertext).replace('x', ' '))
