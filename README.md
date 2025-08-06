#
# @dp.message(F.text == "/start")
# async def blablafunk(message: Message):
#     await message.answer_invoice(
#         title="Buy Diamond",
#         description="Purchase a diamond for your account",
#         payload="unique_payload",
#         provider_token="",
#         currency="XTR",
#         prices=[LabeledPrice(label="Buy Diamond", amount=5)],
#         photo_url="https://i.postimg.cc/cJTBFWPP/Group-10.png",
#         photo_width=300,
#         photo_height=200
#     )