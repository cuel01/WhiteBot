import asyncio
import discord
import random
import re
import os, json
import datetime
from discord.ext import commands
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
        
bot = commands.Bot(command_prefix='/', help_command=None)

class etc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 검색(self, ctx, *, 검색어):
        embed = discord.Embed(title="<a:check:824251178493411368> 검색결과",
                          description="여러 사이트에서 검색한 결과입니다.",
                          color=0xfefefe)
        embed.add_field(name="구글 검색결과",
                    value=('https://www.google.com/search?q=' +
                           검색어.replace(" ", "%20")),
                    inline=False)
        embed.add_field(name="네이버 검색결과",
                    value=('https://search.naver.com/search.naver?query=' +
                           검색어.replace(" ", "%20")),
                    inline=False)
        embed.add_field(name="다음 검색결과",
                    value=('https://search.daum.net/search?w=tot&q=' +
                           검색어.replace(" ", "%20")),
                    inline=False)
        embed.add_field(name="위키백과 검색결과",
                    value=('https://ko.wikipedia.org/wiki/특수:검색/' +
                           검색어.replace(" ", "_")),
                    inline=False)
        embed.add_field(name="지식백과 검색결과",
                    value=('https://terms.naver.com/search.naver?query=' +
                           검색어.replace(" ", "_")),
                    inline=False)
        embed.add_field(name="나무위키 검색결과",
                    value=('https://namu.wiki/Search?q=' +
                           검색어.replace(" ", "%20")),
                    inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def 전송(self, ctx, *, 내용):
        await ctx.send(내용)

    @commands.command()
    async def 암호(self, ctx, *수신문):
        원문 = ' '.join(수신문)
        암호문 = []
        띄쓰방지 = 원문.replace(" ", "")
        띄어쓰기 = ' '.join(띄쓰방지)
        띄쓰리스트 = 띄어쓰기.split()
        for 암호화문자 in 띄쓰리스트:
            암호 = ord(암호화문자)
            암호문.append(암호)
            대괄호생략 = str(암호문).replace(',', '')
        embed = discord.Embed(title="<a:check:824251178493411368> 암호화 완료!",
                          description="아스키 코드를 기반으로 한 암호문입니다.\n해독할 때 띄어쓰기는 인식되지 않으니 `_`나 `-`등의 문자를 넣는것을 추천해요!",
                          color=0xFEFEFE)
        embed.add_field(name="**원문:**",
                    value=f"```{원문}```",
                    inline=False)
        embed.add_field(name="**암호문:**", value=f"```{대괄호생략[1:-1]}```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def 해독(self, ctx, *수신문):
        try:
            원문 = ','.join(수신문)
            원문결과용 = ' '.join(수신문)
            암호문 = []
            for 암호화문자 in 원문.split(','):
                암호 = chr(int(암호화문자))
                암호문.append(암호)
                대괄호생략 = str(암호문).replace(',', '').replace('\'', '')
            embed = discord.Embed(title="<a:check:824251178493411368> 해독 완료!",
                          description="아스키 코드를 기반으로 한 암호문을 해독하였습니다.\n해독이 잘못되었다면 [서포팅 서버](<https://discord.gg/aebSVBgzuG>)에 제보해주세요!",
                              color=0xFEFEFE)
            embed.add_field(name="**암호문:**",
                        value=f"```{원문결과용}```",
                        inline=False)
            embed.add_field(name="**해독 결과:**", value=f"```{대괄호생략[1:-1].replace(' ','')}```", inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send('올바른 암호문을 입력해주세요.')

def setup(bot):
    bot.add_cog(etc(bot))