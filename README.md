# TelBot-IMG_TO_PDF
**Telegram Image to PDF Bot**

This Telegram bot allows users to send images, which are then combined into a PDF file and sent back to the user. The bot is written in Python and uses the `python-telegram-bot` library for interacting with the Telegram API, as well as the `PIL` (Pillow) and `FPDF` libraries for image processing and PDF generation, respectively.

### Setup
1. **Install Dependencies:**
   ```
   pip install python-telegram-bot pillow fpdf
   ```

2. **Telegram Bot API Key:**
   - Create a new bot on Telegram using the BotFather.
   - Copy the API token provided by BotFather.
   - Replace `'YOUR_BOT_API_KEY'` in the code with your actual bot API token.

3. **Folder Structure:**
   Create two folders in the same directory as your Python script:
   - `input`: For storing incoming images.
   - `output`: For storing the generated PDF file.

### Usage
1. **Start the Bot:**
   Run the Python script to start the bot.

2. **Sending Images:**
   - Users can send images as documents to the bot.
   - Use the "/send" command to process and combine all received images into a PDF file.

3. **Sending a Predefined Image:**
   - Use the "/sendpic" command to send a predefined image back to the user.

### Code Overview
- The bot listens for document messages using `MessageHandler` and downloads the images to the `input` folder.
- The `/send` command triggers the `process` function, which combines the images into a single PDF file using `FPDF`.
- The `/sendpic` command sends a predefined image back to the user.

### Note
- Ensure that your bot has permission to access and download files.
- Adjust file paths and names as needed based on your folder structure and requirements.

### Example
```python
# Replace 'YOUR_BOT_API_KEY' with your actual bot API token
bot_key = 'YOUR_BOT_API_KEY'
```

### Credits
- Python Telegram Bot Library: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Pillow Library: [Pillow](https://python-pillow.org/)
- FPDF Library: [FPDF](https://pyfpdf.readthedocs.io/en/latest/)
