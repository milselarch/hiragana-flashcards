import json

raw_text = """
あ	a - father
い	i - eat
う	u - boot
え	e - hen
お	o - open
か	ka - come
き	ki - key
く	ku - cool
け	ke - cake
こ	co - coke
さ	sa - salt
し	shi - she
す	su - sue
せ	se - second
そ	so - son
た	ta - talk
ち	chi - cheek
つ	tsu - sue
て	te - tell
と	to - toe
な	na - none
に	ni - knee
ぬ	nu - new
ね	ne - neck
の	no - no
は	ha - hop
ひ	hi - he
ふ	fu - who
へ	he - hey
ほ	ho - hoe
ま	ma - mom
み	mi - me
む	mu - moo
め	me - met
も	mo - more
や	ya - yacht
ゆ	yu - you
よ	yo - yo
ら	ra - rotten
り	ri - read
る	ru - rude
れ	re - red
ろ	ro - row
わ	wa - water
お	o - oh
ん	n - in
が	ga- god
ぎ	gi-geek
ぐ	gu-google
げ	ge-get
ご	go-go
ぎゃ	gya
ぎゅ	gyu
ぎょ	gyo
ざ	za - pizza
じ	ji - jeap
ず	zu - zoo
ぜ	ze -
ぞ	zo - zodiac
じゃ	ja
じゅ	ju
じょ	jo
だ	da - dot
ぢ	ji - jeap
づ	zu - zoo
で	de - dead
ど	do - dow
じゃ	(ja)
じゅ	(ju)
じょ	(jo)
ば	ba - bob
び	bi - bee
ぶ	bu - boo
べ	be - bed
ぼ	bo - bow
びゃ	bya
びゅ	byu
びょ	byo
ぱ	pa - papa
ぴ	pi - pea
ぷ	pu - poop
ぺ	pe - pet
ぽ	po - police
ぴゃ	pya
ぴゅ	pyu
ぴょ	pyo
""".strip()

# print([char for char in raw_text.split('\n')[0]])

lines = raw_text.split('\n')
cards = []

for line in lines:
    jap_char, hint = line.split('\t')
    cards.append([jap_char, hint])

print(cards)

# Open the file in write mode
with open("flashcards.json", "w") as file:
    # Convert data to JSON and write to the file
    json.dump(cards, file)