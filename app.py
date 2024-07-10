import gradio  as gr
import qrcode
def do(text):
    qrc=qrcode.QRCode(
        version=5,
        box_size=10,
        border=4
    )
    qrc.add_data(text)
    qrc.make(fit=True)
    img=qrc.make_image()
    #img.show()
    img.save('qr.png')
    return 'qr.png'
iface=gr.Interface(fn=do,title='網址生成qr code工具',description='只要輸入一個網址我們就會幫你製造城qr code.',inputs='text',outputs='image')
iface.launch(share=True)
