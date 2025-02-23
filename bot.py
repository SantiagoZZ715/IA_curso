import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from app import validar_cups  # Importamos la función desde app.py

# Configurar el token de Telegram

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

# Configurar logs
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: CallbackContext) -> None:
    """Mensaje de bienvenida"""
    await update.message.reply_text("¡Hola! Envíame un código CUPS, una descripción y el tipo de atención (AP o AC) en el siguiente formato \n\n `CUPS;Descripción;Tipo de Atención`")

async def validate(update: Update, context: CallbackContext) -> None:
    """Procesa el mensaje del usuario"""
    mensaje = update.message.text.split(";")  # Esperamos el mensaje en formato "cups;descripcion;tipo"
    
    if len(mensaje) != 3:
        await update.message.reply_text("⚠️ Formato incorrecto. Envíame el mensaje en este formato:\n\n`CUPS;Descripción;Tipo de Atención`")
        return
    
    cups_ingresado, descripcion, tipo_atencion = mensaje[0].strip(), mensaje[1].strip(), mensaje[2].strip()
    resultado = validar_cups(cups_ingresado, descripcion, tipo_atencion)
    
    await update.message.reply_text(resultado)

async def stop(update: Update, context: CallbackContext) -> None:
    """Cierra el bot de forma segura."""
    await update.message.reply_text("👋 Bot detenido. Hasta luego.")
    context.application.stop()

    
    cups_ingresado, descripcion, tipo_atencion = mensaje[0].strip(), mensaje[1].strip(), mensaje[2].strip()
    resultado = validar_cups(cups_ingresado, descripcion, tipo_atencion)
    
    await update.message.reply_text(resultado)

def main():
    """Inicia el bot"""
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, validate))
    app.add_handler(CommandHandler("stop", stop))

    # Ejecutar el bot
    print("Bot en ejecución...")
    app.run_polling()

if __name__ == "__main__":
    main()
