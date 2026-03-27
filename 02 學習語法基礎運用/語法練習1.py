{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJ5BZRKs3A2vFDNETwnj0Z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ziptee123/coding/blob/main/02%20%E5%AD%B8%E7%BF%92%E8%AA%9E%E6%B3%95%E5%9F%BA%E7%A4%8E%E9%81%8B%E7%94%A8/%E8%AA%9E%E6%B3%95%E7%B7%B4%E7%BF%921.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cS4xSsXzOTy6"
      },
      "outputs": [],
      "source": [
        "print(\"hello,這是我的第一行程式!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=\"小明\"\n",
        "age=20\n",
        "print(name)\n",
        "print(age)"
      ],
      "metadata": {
        "id": "4v-67KOoOn6l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name=\"小明\"\n",
        "food=\"鹽酥雞\"\n",
        "print(f\"我是{name}，我最喜歡吃{food}！\")"
      ],
      "metadata": {
        "id": "hfTSHmzNPuhI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "food=input(\"你今天想吃什麼食物?\")\n",
        "print(f\"真巧，我也想吃{food}\")"
      ],
      "metadata": {
        "id": "WzQxAGtOQ8_O"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "drink=int(input(\"請問這杯飲料多少錢?\"))\n",
        "print(f\"買三杯需要{drink*3}元\")"
      ],
      "metadata": {
        "id": "E97i3L03UfBD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "temp=float(input(\"請問你目前的體溫?\"))\n",
        "if temp>=38:\n",
        "  print(\"你發燒了，禁止進入!\")\n",
        "elif temp<34:\n",
        "  print(\"你的體溫過低，請盡速就醫!\")\n",
        "else:\n",
        "  print(\"體溫正常，可進入!\")"
      ],
      "metadata": {
        "id": "KduCsIlIWew3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "  print(f\"這是我印出的第{i}遍!\")"
      ],
      "metadata": {
        "id": "RPqmNZvdZYj0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "password=\"\"\n",
        "while password!=\"1234\":\n",
        "  password=input(\"請輸入密碼:\")\n",
        "  if password == \"1234\":\n",
        "    print(\"密碼正確。\")\n",
        "  else:\n",
        "    print(\"輸入錯誤。\")"
      ],
      "metadata": {
        "id": "S1Um5Z_daPrJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "  password=input(\"請輸入密碼:\")\n",
        "  if password==\"1234\":\n",
        "    print(\"密碼正確!\")\n",
        "    break\n",
        "  else:\n",
        "    print(\"密碼錯誤!\")"
      ],
      "metadata": {
        "id": "89g-BrQSeE_t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_list=[\"蘋果\",\"香蕉\",\"橘子\"]\n",
        "my_list.append(input(\"請問還要買什麼?\"))\n",
        "for i in my_list:\n",
        "  print(f\"我超想買{i}!\")"
      ],
      "metadata": {
        "id": "Iu7jruvIfgn-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "secret=55\n",
        "history=[]\n",
        "while True:\n",
        "  guess=int(input(\"請猜一個數字:\"))\n",
        "  history.append(guess)\n",
        "  if guess>55:\n",
        "    print(\"太大了!\")\n",
        "  elif guess<55:\n",
        "    print(\"太小了!\")\n",
        "  else :\n",
        "    print(\"正確!\")\n",
        "    break\n",
        "print(f\"你總共猜了這些數字:{history}\")\n",
        "print(f\"你總共猜了{len(history)}次!\")"
      ],
      "metadata": {
        "id": "91JUoLj0iaz1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cart=[]\n",
        "while True:\n",
        "  print(\"==選項==\")\n",
        "  print(\"1.新增物品\")\n",
        "  print(\"2.查看購物車\")\n",
        "  print(\"3.結帳\")\n",
        "  choice = input(\"請輸入選項 (1, 2, 3)：\")\n",
        "  if choice==\"1\":\n",
        "    add=input(\"想買什麼?\")\n",
        "    cart.append(add)\n",
        "    print(f\"已經將{add}加入購物車。\")\n",
        "  elif choice==\"2\":\n",
        "    print(f\"目前共有{len(cart)}項物品!\")\n",
        "    print(f\"你總共買了:{cart}\")\n",
        "  elif choice==\"3\":\n",
        "    print(\"歡迎下次光臨!\")\n",
        "    break\n",
        "  else:\n",
        "    print(\"沒有這個選項!\")"
      ],
      "metadata": {
        "id": "V5gnUO-_KfM6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "餘額=1000\n",
        "while True:\n",
        "  print(\"==選項==\")\n",
        "  print(\"1.查詢餘額 2.存錢 3.提款 4.退出\")\n",
        "  choice=input(\"請輸入選項(1,2,3,4):\")\n",
        "  if choice==\"1\":\n",
        "    print(f\"目前餘額為{餘額}元!\")\n",
        "  elif choice==\"2\":\n",
        "    add=int(input(\"請輸入存款金額:\"))\n",
        "    餘額=餘額+(add)\n",
        "    print(f\"已存入{add}元!\")\n",
        "    print(f\"目前餘額為{餘額}元!\")\n",
        "  elif choice==\"3\":\n",
        "    det=int(input(\"請輸入提款金額:\"))\n",
        "    if det>餘額:\n",
        "      print(\"餘額不足!\")\n",
        "    else:\n",
        "      餘額=餘額-(det)\n",
        "      print(f\"已提款{det}元!\")\n",
        "      print(f\"目前餘額為{餘額}元!\")\n",
        "  elif choice==\"4\":\n",
        "    print(\"請拿回信用卡。\")\n",
        "    break\n",
        "  else:\n",
        "    print(\"沒有這個選項!\")"
      ],
      "metadata": {
        "id": "INI23QlMUcMm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "slime_hp=50\n",
        "while slime_hp>0:\n",
        "  print(\"1.普通攻擊\" \"2.大招\")\n",
        "  attack=input(\"使用技能(1、2)\")\n",
        "  if attack==\"1\":\n",
        "    slime_hp=slime_hp-5\n",
        "    print(f\"史萊姆受到傷害!目前血量:{slime_hp}\")\n",
        "  elif attack==\"2\":\n",
        "    slime_hp=slime_hp-10\n",
        "    print(f\"史萊姆受到傷害!目前血量:{slime_hp}\")\n",
        "  else:\n",
        "    slime_hp=slime_hp-0\n",
        "    print(f\"技能無效!目前血量:{slime_hp}\")\n",
        "print(\"戰鬥結束!\")\n"
      ],
      "metadata": {
        "id": "4HOp3LGzZKMq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "menu={\"紅茶\":30,\"奶茶\":45,\"綠茶\":25}\n",
        "total=0\n",
        "while True:\n",
        "  print(menu)\n",
        "  order=input(\"請問要喝什麼?(按下結帳以結束)\")\n",
        "  if order in menu:\n",
        "    total=total+menu[order]\n",
        "    print(f\"總花費{total}元。\")\n",
        "  elif order==\"結帳\":\n",
        "    break\n",
        "  else:\n",
        "    print(\"沒有賣這個喔!\")\n",
        "print(f\"你總共要花{total}元。\")"
      ],
      "metadata": {
        "id": "vxH2XLlo5j4z"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}