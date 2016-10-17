import config
import datetime
from flask import Flask, request, render_template, send_from_directory, redirect
from forms import UserTextField
from pyqrcode import QRCode


app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    qr_file_name = None
    if request.method == 'POST':
        form = UserTextField(request.form)
        if form.validate():
            qr_code = QRCode(form.data['text'], encoding='utf-8')
            qr_file_name = 'tmp/' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '.png'
            qr_code.png(qr_file_name, scale=5)
            if form.data['mode'] == 'download':
                return redirect(qr_file_name)
    else:
        form = UserTextField()

    return render_template(
        'index.html',
        form=form,
        link=qr_file_name,
        )


@app.route('/tmp/<path:qr_path>')
def show_qr(qr_path):
    return send_from_directory('tmp', qr_path, as_attachment=True)


if __name__ == '__main__':
    app.run()
