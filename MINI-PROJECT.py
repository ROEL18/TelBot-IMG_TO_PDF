from PIL import Image
from fpdf import FPDF
import os
import os

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

i = 0

bot_key = ''


def send_about(update: Update, context: CallbackContext) -> None:
    context.bot.send_document(chat_id=update.message['chat']['id'], document=open(
        r'', 'rb'), filename='about.png')


def downloader(update, context):
    global i

    context.bot.get_file(update.message.document).download(f"input/{i}.jpg")
    i = i+1
    update.message.reply_text("Image recived")

    img_path = "input/input.jpg"
    pdf_path = "output/output.pdf"


def process(update: Update, context: CallbackContext):
    update.message.reply_text("Generating Pdf")

    image_list = os.listdir('input/')
    '''output = []
    for i in image_list:
        output.append(Image.open(rf'input/{i}').convert('RGB'))
    im = output[0]
    im.save(r"output/output.pdf", save_all=True,
            append_images=image_list)

    # im_4 = image_4.convert('RGB')

    # image_list = [im_2, im_3, im_4]'''

    pdf = FPDF()
    for image in image_list:
        pdf.add_page()
        pdf.image(f"input/{image}", 0, 0, 297, 210)
    pdf.output("output/output.pdf", "F")

    context.bot.send_document(chat_id=update.message['chat']['id''id'], document=open(
        r"output\output.pdf", 'rb'), filename='out.pdf')
    os.remove(r'output/output.pdf')
    for img in image_list:
        os.remove(f"input/{img}")


updater = Updater(bot_key)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.document, downloader))
dispatcher.add_handler(CommandHandler("sendpic", send_about))
updater.dispatcher.add_handler(CommandHandler('send', process))


updater.start_polling()

