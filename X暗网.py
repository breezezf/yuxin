import streamlit as st
from PIL import Image
page=st.sidebar.radio("X暗网",["我的名片","我的图片处理工具","我的智慧词典","我的留言区","知识拓展","每周一道选择题"])
def page_1():
    st.balloons()
    likes=0
    st.write(":yellow[作者:黑幕]")
    st.write(":red[爱好：没啥爱好]")
    st.write(":blue[特长:无]")
    st.write("真名：秘密")
    if st.button("不要按"):
        st.write("真名在彩蛋中，自己去寻找吧！")
    st.write("完成非常辛苦，请点赞")
    if st.button("点赞"):
        likes+=1
    st.write("点赞数：",likes)
def page_2():
    st.write(":blue[:sunglasses:图片处理小程序:sunglasses:]")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,2,0,1))
        
def page_3():
    st.write("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt","w",encoding="utf-8")as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write("查询次数为：",times_dict[n])
def page_4():
    st.write("我的留言板")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        message_list=f.read().split("\n")
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split("#")
    for i in message_list:
        if i[1]=="阿短":
            with st.chat_message("🐔"):
                st.write(i[1],":",i[2])
        elif i[1]=="编程猫":
            with st.chat_message("🌀"):
                st.write(i[1],":",i[2])
    name=st.selectbox("我是……",["阿短","编程猫"])
    new_message=st.text_input("想要写什么……")
    if st.button("留言"):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message=''
            for i in message_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
                print(message)
            message=message[:-1]
            f.write(message)
def page_5():
    st.write("每周一更新栏")
    tab1,tab2,tab3,tab4=st.tabs(["001","002","003","彩蛋"])
    with tab1:
        st.write("更新中~~")
    with tab2:
        st.write("没想到吧！正文在这里！")
        st.write("舒庆春，字舍予，笔名老舍，满族正红旗人，本名舒庆春，生于北京，中国现代小说家、著名作家，杰出的语言大师、人民艺术家，新中国第一位获得“人民艺术家”称号的作家。著有长篇小说《小坡的生日》、《猫城记》、《牛天赐传》、《骆驼祥子》等，短篇小说《赶集》等。老舍的文学语言通俗简易，朴实无华，幽默诙谐，具有较强的北京韵味。1966年8月24日，中国作家老舍因不堪忍受红卫兵的暴力批斗，在北京太平湖投湖自尽。1978年初，老舍得到平反，恢复了“人民艺术家”的称号。")
        st.write('----')
        news =st.radio(
        '选择：老舍死因',
        ['寿终正寝','病逝','被军队打死','投湖自杀'],
        )
        message = ''
        if news== "寿终正寝":
            message = '大错特错'
        elif news== "病逝":
            message = '差了十万八千里'
        elif news== "被军队打死":
            message = '很接近，但不对'
        elif news=="投湖自杀":
            message = '正确！！！(历史上将此次事件称之为：文化大革命)'
        st.write(message)
    with tab3:
        st.write("接下去来说说古代的作家吧！")
        st.write("李白（701年2月28日—762年12月），字太白，号青莲居士，祖籍陇西成纪（今甘肃省秦安县），出生于西域碎叶（在今吉尔吉斯斯坦境内）。唐朝伟大的浪漫主义诗人，凉武昭王李暠九世孙 。为人爽朗大方，乐于交友，爱好饮酒作诗，名列“酒中八仙” 。曾经得到唐玄宗李隆基赏识，担任翰林供奉 ，赐金放还，游历全国，先后迎娶宰相许圉师、宗楚客的孙女。唐肃宗李亨即位后，卷入永王之乱，流放夜郎，辗转到达当涂县令李阳冰家。上元二年，去世，时年六十二 。著有《李太白集》，代表作有《望庐山瀑布》《行路难》《蜀道难》《将进酒》《早发白帝城》《黄鹤楼送孟浩然之广陵》等 [2]。李白所作词赋，就其开创意义及艺术成就而言，享有极为崇高的地位，后世誉为“诗仙”，与诗圣杜甫并称“李杜”。")
        st.write('----')
        news =st.radio(
        '选择：李白故乡',
        ['哈萨克斯坦','塔吉克斯坦','吉尔吉斯斯坦','土库曼斯坦'],
        )
        message = ''
        if news== "哈萨克斯坦":
            message = '大错特错'
        elif news== "塔吉克斯坦":
            message = '差了十万八千里'
        elif news== "土库曼斯坦":
            message = '很接近，但不对'
        elif news=="吉尔吉斯斯坦":
            message = '正确！！！'
        st.write(message)        
    with tab4:
        search=0
        if st.button("真名"):
            st.write("庞俞昕")
            search+=1
            st.write("你是第",search,"个找到它的")
def page_6():
# 如何创建单选框？
# 单选框中的两个必填参数分别是？都有什么作用？
# captions参数的作用是？

# 挑战：根据选项显示对应的颜色
    st.write('----')
    st.write("每周一题（时事政治）")
    st.image("下载图片.jpg")
    news =st.radio(
        '选择：2024年1月27日谁在亚丁湾袭击了英国货轮',
        ['美国得克萨斯州部队','大明水师','伊拉克人民军','也门胡塞武装'],
    )
    message = ''
    if news== "美国得克萨斯州部队":
        message = '大错特错'
    elif news== "大明水师":
        message = '差了十万八千里'
    elif news== "伊拉克人民军":
        message = '很接近，但不对'
    elif news=="也门胡塞武装":
        message = '正确！！！'
    st.write(message)

    def img_change(img,rc,gc,bc):
        width,height=img.size
        img_arrey=img.load()
        for x in range(width):
            for y in range(height):
                r=img_arrey[x,y][rc]
                g=img_arrey[x,y][gc]
                b=img_arrey[x,y][bc]
                img_arrey[x,y]=(b,g,r)
        return img
if page=="我的名片":
    page_1()
elif page=="我的图片处理工具":
    page_2()
elif page=="我的智慧词典":
    page_3()
elif page=="我的留言区":
    page_4()
elif page=="知识拓展":
    page_5()
elif page=="每周一道选择题":
    page_6()
