import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = 'MTA3MDgyOTcyNzgyNjMyNTU0NQ.GIKUuV.v-jS1IgSNpWBKW6EPkbVhGB1xjPuGjCyl5jVmI'
shop1 = '𝐏𝐈𝐆 𝐒𝐇𝐎𝐏'
shop2 = 'https://cdn.discordapp.com/attachments/934504890447855646/1070739762043945020/discord-avatar-512-22IHL.png'


@client.event
async def on_ready():
    print("봇 아이디: ", client.user.id)
    print("봇 준비 완료")
    await bt(['𝐏𝐈𝐆 𝐒𝐇𝐎𝐏'])

async def bt(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game(g))
            await asyncio.sleep(5)

        ch = 0
        for g in client.guilds:
            ch += len(g.channels)

@client.event
async def on_message(message):

    if message.content.startswith('!부스트'):
        await message.delete()
        embed=discord.Embed(title="``💎 𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝐁𝐎𝐎𝐒𝐓 💎``", description=f"[제품소개](https://support.discord.com/hc/ko/articles/360028038352--%EC%84%9C%EB%B2%84-%EB%B6%80%EC%8A%A4%ED%8C%85-%EC%9E%90%EC%A3%BC-%EB%AC%BB%EB%8A%94-%EC%A7%88%EB%AC%B8-)", colour=discord.Colour.blue())
        embed.add_field(name="``💎𝐁𝐎𝐎𝐒𝐓 2개 ( 3개월 )``", value="``💳가격 : 1,000원``", inline=False)
        embed.add_field(name="``💎𝐁𝐎𝐎𝐒𝐓 8개 ( 3개월 )``", value="``💳가격 : 3,000원``", inline=False)
        embed.add_field(name="``💎𝐁𝐎𝐎𝐒𝐓 14개 ( 3개월 )``", value="``💳가격 : 5,000원``", inline=False)
        embed.add_field(name="", value="``* 부스트 토큰 추방 시 부스트가 없어집니다.``", inline=False)
        embed.add_field(name="", value="``* 부스트 토큰 추방으로 인한 환불, 교환은 불가능합니다!``", inline=False)
        embed.add_field(name="", value='``* 문화상품권으로 구매시 수수료 + 15% 입니다``', inline=False)
        embed.set_image(url='https://media.discordapp.net/attachments/934504890447855646/1073812638183723129/discord-nitro.gif')
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send(embed=embed)

    if message.content.startswith('!베이직'):
        await message.delete()
        embed=discord.Embed(title="``🌌𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗡𝗜𝗧𝗥𝗢 𝐁𝐀𝐒𝐈𝐂🌌``", description=f"[제품설명](https://support.discord.com/hc/ko/articles/115000435108-Discord-Nitro-Classic-Nitro)", colour=discord.Colour.blurple())
        embed.add_field(name='``🌌𝗡𝗜𝗧𝗥𝗢 𝐁𝐀𝐒𝐈𝐂 1𝗠𝗢𝗡𝗧𝗛 ( 선물 )``', value='``💳가격 : 5,000원``', inline=False)
        embed.add_field(name='``🌌𝗡𝗜𝗧𝗥𝗢 𝐁𝐀𝐒𝐈𝐂 1𝗬𝗘𝗔𝗥 ( 선물 )``', value='``💳가격 : 46,000원``', inline=False)
        embed.add_field(name="``🌌𝗡𝗜𝗧𝗥𝗢 𝐁𝐀𝐒𝐈𝐂 1𝗠𝗢𝗡𝗧𝗛 ( 계정방식 )``", value="``💳가격 : 3,500원``", inline=False)
        embed.add_field(name="``🌌𝗡𝗜𝗧𝗥𝗢 𝐁𝐀𝐒𝐈𝐂 1𝗬𝗘𝗔𝗥 ( 계정방식 )``", value="``💳가격 : 22,000원``", inline=False)
        embed.set_image(url='https://media.discordapp.net/attachments/934504890447855646/1073813244159983686/CompetentJovialAnkolewatusi-size_restricted.gif')
        await message.channel.send(embed=embed)
        
    if message.content.startswith('!프라임'):
        await message.delete()
        embed=discord.Embed(title="``🚀𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗡𝗜𝗧𝗥𝗢 𝐏𝐑𝐈𝐌𝐄🚀``", description=f"[제품설명](https://support.discord.com/hc/ko/articles/115000435108-Discord-Nitro-Classic-Nitro)", colour=discord.Colour.blurple())
        embed.add_field(name='``🚀𝗡𝗜𝗧𝗥𝗢 𝐏𝐑𝐈𝐌𝐄 1𝗠𝗢𝗡𝗧𝗛 ( 선물 )``', value='``💳가격 : 7,500원``', inline=False)
        embed.add_field(name='``🚀𝗡𝗜𝗧𝗥𝗢 𝐏𝐑𝐈𝐌𝐄 1𝗬𝗘𝗔𝗥 ( 선물 )``', value='``💳가격 : 70,000원``', inline=False)
        embed.add_field(name="``🚀𝗡𝗜𝗧𝗥𝗢 𝐏𝐑𝐈𝐌𝐄 1𝗠𝗢𝗡𝗧𝗛 ( 계정방식 )``", value="``💳가격 : 4,500원``", inline=False)
        embed.add_field(name="``🚀𝗡𝗜𝗧𝗥𝗢 𝐏𝐑𝐈𝐌𝐄 1𝗬𝗘𝗔𝗥 ( 계정방식 )``", value="``💳가격 : 35,000``", inline=False)
        embed.set_image(url='https://media.discordapp.net/attachments/934504890447855646/1073813244159983686/CompetentJovialAnkolewatusi-size_restricted.gif')
        embed.set_footer(text='🐽 𝓟𝓘𝓖 𝓢𝓗𝓞𝓟 🐽', icon_url='https://cdn.discordapp.com/attachments/934504890447855646/1070739762043945020/discord-avatar-512-22IHL.png')
        await message.channel.send(embed=embed)

    if message.content.startswith('!스포티파이'):
        await message.delete()
        embed=discord.Embed(title="``🎶𝐒𝐏𝐎𝐓𝐈𝐅𝐘🎶``", description=f"[제품설명](https://www.spotify.com/kr-ko/premium/&ab=false/)", colour=discord.Colour.green())
        embed.add_field(name="``🎶𝐒𝐏𝐎𝐓𝐈𝐅𝐘 일반 ( 무제한 )``", value="``💳가격 : 3,000원``", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/934504890447855646/1077495653598498846/Spotify.gif")
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send(embed=embed)

    if message.content.startswith('!디즈니'):
        await message.delete()
        embed=discord.Embed(title="``🎀𝐃𝐈𝐒𝐍𝐄𝐘 𝐏𝐋𝐔𝐒🎀``", description=f"[제품설명](https://www.disneyplus.com/ko-kr/welcome/stream?cid=DSS-Search-Google-71700000088339394-&s_kwcid=AL%218468%213%21620347232144%21e%21%21g%21%21%EB%94%94%EC%A6%88%EB%8B%88+%ED%94%8C%EB%9F%AC%EC%8A%A4&gclid=CjwKCAiA_vKeBhAdEiwAFb_nrcLomTWYxN6HGU3w2D6__jZKQxMXqkOge5cA5Ji-3WoBrjI6UXlTjBoCX7MQAvD_BwE&gclsrc=aw.ds)",color=discord.Colour.blurple())
        embed.add_field(name="``🎀𝐃𝐈𝐒𝐍𝐄𝐘 𝐏𝐋𝐔𝐒 ( 랜덤계정 )``", value="``💳가격 : 500원``", inline=False)
        #embed.add_field(name="", value="``* 불량률 1%``", inline=False)
        embed.add_field(name="", value="``* 첫 구매시 보상 1번 해드립니다``", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/934504890447855646/1078508000643391558/giphy.gif")
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send(embed=embed)

    #if message.content.startswith('!디즈니'):
        await message.delete()
        embed=discord.Embed(title="``🎀𝐃𝐈𝐒𝐍𝐄𝐘 𝐏𝐋𝐔𝐒 𝐎𝐌𝐄𝐆𝐀🎀``", description=f"[𝐃𝐈𝐒𝐍𝐄𝐘](https://www.disneyplus.com/ko-kr/welcome/stream?cid=DSS-Search-Google-71700000088339394-&s_kwcid=AL%218468%213%21620347232144%21e%21%21g%21%21%EB%94%94%EC%A6%88%EB%8B%88+%ED%94%8C%EB%9F%AC%EC%8A%A4&gclid=CjwKCAiA_vKeBhAdEiwAFb_nrcLomTWYxN6HGU3w2D6__jZKQxMXqkOge5cA5Ji-3WoBrjI6UXlTjBoCX7MQAvD_BwE&gclsrc=aw.ds)",color=discord.Colour.blurple())
        embed.add_field(name="``🎀𝐃𝐈𝐒𝐍𝐄𝐘 𝐏𝐋𝐔𝐒 𝐎𝐌𝐄𝐆𝐀``", value="``💳가격 : 500원``", inline=False)
        embed.add_field(name="", value="``* 계정 불량률 1%``", inline=False)
        embed.add_field(name="", value="``* 𝐔𝐇𝐃 화질``", inline=False)
        embed.add_field(name="", value="``* 3개당 1개 교환 가능 ( 구매후 5분 이내 )``")
        embed.set_image(url="https://cdn.discordapp.com/attachments/934504890447855646/1078508000643391558/giphy.gif")
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send(embed=embed)

    if message.content.startswith("!넷플릭스"):
        await message.delete()
        embed=discord.Embed(title="``🎬𝐍𝐄𝐓𝐅𝐋𝐈𝐗 𝐎𝐌𝐄𝐆𝐀🎬``", description=f"[𝐍𝐄𝐓𝐅𝐋𝐈𝐗](https://www.netflix.com)", color=0xE74C3C)
        embed.add_field(name="``🎬𝐍𝐄𝐓𝐅𝐋𝐈𝐗 𝐎𝐌𝐄𝐆𝐀``", value="``💳가격 : 500원``", inline=False)
        embed.add_field(name="", value="``* 계정 불량률 3%``", inline=False)
        embed.add_field(name="", value="``* 𝐔𝐇𝐃 화질``", inline=False)
        embed.add_field(name="", value="``* 프리미엄, 스탠다드 요금제만``", inline=False)
        embed.add_field(name="", value="``* 3개당 1개 교환 가능 ( 구매후 5분 이내 )``")
        embed.set_image(url="https://media.discordapp.net/attachments/934504890447855646/1077494556976742410/deu6ibr-370dd0cc-05f0-4402-be5f-0b2e265a907b.gif")
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send(embed=embed)

    if message.content == "s.도움말":
        embed = discord.Embed(title="봇 명령어", description=" ", color=0x62c1cc)
        embed.set_author(name="Siro Bot", icon_url="https://cdn.discordapp.com/attachments/796918898112856116/834310676028850216/11529_6EoYCLs5.png")
        embed.add_field(name=" 도박 ", value=" s.도박 < 금액 >", inline=True)
        embed.add_field(name=" 돈 ", value="s.돈 < 현재 잔고 안내 >", inline=False)
        embed.add_field(name=" 돈받기 ", value="s.돈받기 < 1시간 마다 돈을 받을실수 있습니다. >", inline=False)
        embed.add_field(name=" 올인 ", value="s.올인 < 가지고 있는 돈을 모두다 도박에 사용합니다. >", inline=False)
        embed.add_field(name=" 랭킹 ", value="s.랭킹 < 누가 제일 돈을 많이 가지고 있는 랭킹으로 표시해줍니다. >", inline=False)
        embed.add_field(name=" 멜론차트 ", value="s.멜론차트 < 실시간 멜론차트 표시 > ", inline=False)
        embed.add_field(name=" 내정보 ", value="s.내정보 < 준비중 > ", inline=False)
        embed.add_field(name=" 청소 ", value="s.청소 < 청소할 메세지 갯수 > < 관리자만 사용가능 >", inline=False)
        embed.add_field(name=" 주사위 ", value="s.주사위 < 랜덤으로 번호를 뽑아줍니다. >", inline=False)
        embed.add_field(name=" 핑 ", value="s.핑 < 현재 핑 상태를 알려줍니다. >", inline=False)
        embed.set_footer(text="Make • Siro#5338", icon_url="https://cdn.discordapp.com/attachments/796918898112856116/834310676028850216/11529_6EoYCLs5.png")
        await message.channel.send('', embed=embed)

    if message.content == "!상태":
        await message.delete()
        embed = discord.Embed(title="``⏰ 관리자 상태 ⏰``", description="", color=0xEB459E)
        embed.add_field(name="``🟢 온라인``", value="``1 ~ 5분내에 답장 가능``", inline=False)
        embed.add_field(name="``🌙 자리비움``", value="``1 ~ 2시간내에 답장 가능``", inline=False)
        embed.add_field(name="``⛔ 다른용무중``", value="``퇴근 OR 답장 불가능``", inline=False)
        embed.add_field(name="``⚫ 오프라인``", value="``퇴근``", inline=False)
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send('', embed=embed)

    if message.content == "!영업":
        await message.delete()
        embed = discord.Embed(title="``⏰ 영업시간 ⏰``",description="", color=0xEB459E)
        embed.add_field(name="``📆 평일``", value="``오후 5시 ~ 오후 11시``", inline=False)
        embed.add_field(name="``📅 주말``", value="``오후 1시 ~ 오전 2시``", inline=False)
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send('', embed=embed)

    if message.content == "!리셀":
        await message.delete()
        embed= discord.Embed(title="``💳 리셀러 모집 💳``", description="주마다 일정 금액을 지불하시면 리셀러가 되실수 있습니다", color=0xFEE75C)
        embed.add_field(name="``💖 조건``", value='``서버인원 50명이상``', inline=False)
        embed.add_field(name="``💵 요금``", value='• 1주일 - ``10,000원``\n • 3주일 - ``25,000원``\n • 6주일 - ``50,000원``\n • 1년 - ``85,000원``\n • 평생 ``120,000원``', inline=False)
        embed.add_field(name="리셀서버 : https://discord.gg/HFfG8gJtrw", value="", inline=False)
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send('', embed=embed)

    if message.content == "!인증":
        await message.delete()
        embed = discord.Embed(title="``💠 인증 방법 💠``", description="``리셀서버 인증 방법입니다!``", color=0xFEE75C)
        embed.add_field(name="``💖 조건``", value="``서버인원 50명이상!``", inline=False)
        embed.add_field(name="``💵 요금``", value='• 1주일 - ``10,000원``\n • 3주일 - ``25,000원``\n • 6주일 - ``50,000원``\n • 1년 - ``85,000원``\n • 평생 ``120,000원``', inline=False)
        embed.add_field(name="``✅ 인증``", value='``• 밑에 있는 티켓을 열어주세요``\n``• 티켓에 있는 계좌로 리셀가격을 입금해주시고 캡쳐해주세요``\n``• 캡처한 사진을 티켓에 보내주시고 서버링크를 보내주세요``', inline=False)
        embed.set_footer(text=shop1, icon_url=shop2)
        await message.channel.send('', embed=embed)

client.run(token) 