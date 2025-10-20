from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8465483999:AAErmPE_a-mqlYyo8fvR-lMnav68Jsipmqs"
ADMIN_USERNAME = "Richard_fx010"

# ---- Start Command ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 VIP Monthly - $30.00", callback_data="vip_monthly")],
        [InlineKeyboardButton("👤 Contact Admin", callback_data="contact")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "✅ *Trade With Richard FX 📈*\n\n"
        "🏅 *GBPUSD*\n"
        "🏅 *EURUSD*\n"
        "🏅 *EURGBP*\n"
        "🏅 *US30*\n"
        "🏅 *S&P500*\n\n"
        "Tap on the following products below to subscribe 👇",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# ---- Button Handler ----
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- VIP PRODUCT DETAIL ---
    if query.data == "vip_monthly":
        keyboard = [
            [InlineKeyboardButton("✅ Accept", callback_data="accept_terms")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_to_menu")]
        ]
        await query.edit_message_text(
            "💎 *VIP Monthly - $30.00*\n\n"
            "Gain access to our *VIP channel* on Telegram for one month by subscribing to this plan.\n\n"
            "Comes with mostly *swing and day trading signals weekly* 📊.\n\n"
            "Tap *Accept* below to continue.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # --- ACCEPT → SHOW TERMS ---
    elif query.data == "accept_terms":
        keyboard = [
            [InlineKeyboardButton("💰 Confirm Purchase", callback_data="confirm")],
            [InlineKeyboardButton("⬅️ Back", callback_data="vip_monthly")]
        ]
        terms_text = (
            "📜 *TERMS AND CONDITIONS*\n\n"
            "1️⃣ *Overview*\n"
            "By purchasing access to this private Telegram signal group, you agree to the following Terms and Conditions. "
            "Please read them carefully before making any payment.\n\n"
            "2️⃣ *Service Description*\n"
            "This group provides Forex and Stock market trading signals and educational content to assist members "
            "in their personal trading journey. All signals and analyses shared are based on market observations "
            "and do not guarantee profit.\n\n"
            "3️⃣ *Access*\n"
            "Access to the private Telegram group is granted only after successful payment confirmation.\n\n"
            "Each membership is personal and non-transferable. Sharing signals or access with others is strictly prohibited.\n\n"
            "The admin reserves the right to remove any member who violates group rules or leaks content without prior notice.\n\n"
            "4️⃣ *Payments*\n"
            "Payments are processed through the Telegram bot or approved crypto payment options.\n\n"
            "Once access is granted, no refund will be issued under any circumstances. Please be sure of your purchase before proceeding.\n\n"
            "5️⃣ *Risk Disclaimer*\n"
            "I am not a financial advisor. All signals and analyses shared are for educational and informational purposes only.\n\n"
            "Trading in Forex and Stocks involves a high level of risk, and you may lose part or all of your investment.\n\n"
            "Members are advised to apply proper risk management and never trade with money they cannot afford to lose.\n\n"
            "Past performance or historical results do not guarantee future returns.\n\n"
            "6️⃣ *Limitation of Liability*\n"
            "The admin and signal providers shall not be held liable for any loss, damage, or financial harm arising directly "
            "or indirectly from the use of the signals or educational materials provided in the group.\n\n"
            "7️⃣ *Privacy Policy*\n"
            "All user data, including payment information, will be handled confidentially and will not be shared with third parties, "
            "except as required by law.\n\n"
            "8️⃣ *Amendments*\n"
            "The admin reserves the right to modify or update these Terms and Conditions at any time without prior notice. "
            "Updated versions will be posted in the group or bot for members to review.\n\n"
            "9️⃣ *Acceptance*\n"
            "By joining the group or making a payment, you acknowledge that you have read, understood, "
            "and agreed to these Terms and Conditions in full."
        )
        await query.edit_message_text(terms_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    # --- CONFIRM PURCHASE (PAYMENT METHODS) ---
    elif query.data == "confirm":
        keyboard = [
            [InlineKeyboardButton("💳 Visa / Mastercard", callback_data="visa")],
            [InlineKeyboardButton("💰 USDT", callback_data="usdt")],
            [InlineKeyboardButton("₿ Bitcoin", callback_data="btc")],
            [InlineKeyboardButton("⬅️ Back", callback_data="accept_terms")]
        ]
        await query.edit_message_text(
            "💵 *Select your preferred payment method below:*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # --- PAYMENT DETAILS ---
    elif query.data in ["visa", "usdt", "btc"]:
        methods = {
            "visa": "💳 *Visa / Mastercard*\nPay securely through our official page: https://flutterwave.com/pay/f0uxf1jpsgjf",
            "usdt": "💰 *USDT (TRC-20)*\nSend to: `TDRd4DZHXwmy7hxFzsd48Yb4DwfKUYrLAc`\nConfirm payment by sending proof to admin.",
            "btc": "₿ *Bitcoin*\nSend BTC to: `bc1qe2lmyay4pqpeq3c7l4akh9jsrlj0s57spk7lh0`\nConfirm payment by sending proof to admin.",
        }
        await query.edit_message_text(
            f"{methods[query.data]}\n\nAfter payment, send proof to the admin for confirmation.",
            parse_mode="Markdown"
        )

    # --- CONTACT ADMIN ---
    elif query.data == "contact":
        contact_link = f"https://t.me/{ADMIN_USERNAME}"
        await query.edit_message_text(
            f"👤 *Contact Admin*\n\nIf you have questions or want to confirm payment, click below to chat with the admin:\n👉 [Message Admin]({contact_link})",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

    # --- BACK BUTTONS ---
    elif query.data == "back_to_menu":
        await start(update, context)

# ---- Main ----
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()