import streamlit as st
# st.header('優しい')
# st.subheader('家族想い')
# st.write('趣味：海外旅行')
# st.write('')

#-----------閏年判定-----------------
# import streamlit as st
# #suuji=int(input("西暦:"))
# st.header('閏年判定ゲーム！')
# suuji=st.number_input('年を入力してください',min_value=0,step=1)
# def birth(suuji):
#     if(suuji<1582):
#         st.write("閏年は存在しない")
#     elif(suuji%100==0 and suuji%400!=0):
#         st.write("平年")
#     elif(suuji%4==0):
#         st.write("閏年")
#     else:
#         st.write("平年")


# btn = st.button('判定！')
# if btn:
#     birth(suuji)
#-----------閏年判定-----------------



#--------------ChatGPT------------------------------
# import streamlit as st

# # ページの設定
# st.set_page_config(
#     page_title="自己紹介アプリ",
#     page_icon="👋",
#     layout="centered",
#     initial_sidebar_state="auto",
# )

# # サイドバーにプロフィール画像と基本情報
# with st.sidebar:
#     st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGzBHrZR334ROAc1y-cGbtIkb_FILsa2ilnjB8iEKnAZeLVh8BFvEwao04gC7_cE7H2hOPlvbjxAe-g_GQ_t4p8xEApWp-T_1OfbZ3Mz-7qjePShZA_5smhC21EG13t_ybgMVGPo3hJA6kjlyrF-Hjyg=/fb_top01.png?errorImage=false", width=150)  # プロフィール画像のURL
#     st.title("自己紹介")
#     st.markdown("09042535067 連絡先")
#     st.markdown("- **Email**: yuta20020629@gamil.com")
#     st.markdown("- **GitHub**: [GitHub](https://github.com/openai)")

# # メインページ
# st.title("👋 こんにちは！私は中村優太です。")

# st.write("""
# 私はとても明るくて優しい人間です！
# """)

# # ユーザー入力によるパーソナライズ
# st.header("✨ あなたの名前を教えてください！")
# user_name = st.text_input("名前を入力してください:")

# if user_name:
#     st.success(f"こんにちは、{user_name}さん！😊 よろしくお願いします！")

# # プロフィールセクション
# st.header("📚 プロフィール")

# with st.expander("🔍 詳細を見る"):
#     st.subheader("趣味")
#     st.write("- 海外旅行")
#     st.write("- 読書")
#     st.write("- 温泉巡り")
    
#     st.subheader("スキル")
#     st.write("- 野球")
#     st.write("- python？？？？？")
#     st.write("- 英語？？？？")
    
#     st.subheader("経験")
#     st.write("""
#     - **インターン**: 10社
#     - **本選考**: 8社（3社内定)
#     """)

# # インタラクティブな要素
# st.header("🎨 カスタマイズ")

# favorite_color = st.color_picker("好きな色を選んでください:", "#00f900")
# st.markdown(f"### あなたの選んだ色: {favorite_color}")
# st.markdown(
#     f"""
#     <style>
#     .custom-background {{
#         background-color: {favorite_color};
#         padding: 10px;
#         border-radius: 5px;
#         color: white;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown('<div class="custom-background">このセクションの背景色はあなたが選んだ色です！</div>', unsafe_allow_html=True)

# # フッター
# st.markdown("---")
# st.markdown("© 2024 ChatGPT | Powered by OpenAI")
#--------------ChatGPT------------------------------



#---------------自己紹介---------------------
st.title("中村優太について知ろう！！！！！！！！")
gakka = st.radio("学科を選択してください",('趣味','部活','就職'))
if gakka != '趣味':
    st.warning("海外旅行、")
else:
    st.write("素晴らしい")
