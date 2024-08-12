import io
import requests
import json
import base64
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

app = Flask(__name__)
api = Api(app)

class GenCert(Resource):
    def get(self):
        return {'version': '1.0.0'}

    def post(self):

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        # print(request.json.get('name'));

        image = ''
        if request.json.get('name') is not None and request.json.get('project') is not None and request.json.get('type') is not None:

            name = request.json.get('name')
            project = request.json.get('project')
            type = request.json.get('type')

            # Custom font style and font size
            font30 = ImageFont.truetype('./cert_files/fonts/Niramit-Regular.ttf', 40)
            font24 = ImageFont.truetype('./cert_files/fonts/Niramit-Regular.ttf', 32)

            w = 1900
            l = 900

            if type == 'TX':
                img = Image.open('./cert_files/frame/TX.jpg')
                I1 = ImageDraw.Draw(img)
                _, _, w1, h1 = I1.textbbox((0, 0), name, font=font30)
                I1.text((l+round((w-l-w1)/2), 500), name, font=font30, fill =(0, 0, 0))

                ptext = project.split('\n')
                if len(ptext) > 0:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[0], font=font24)
                    I1.text((l+round((w-l-w2)/2), 650), ptext[0], font=font24, fill =(0, 0, 0))
                if len(ptext) > 1:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[1], font=font24)
                    I1.text((l+round((w-l-w2)/2), 690), ptext[1], font=font24, fill =(0, 0, 0))
                if len(ptext) > 2:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[2], font=font24)
                    I1.text((l+round((w-l-w2)/2), 730), ptext[2], font=font24, fill =(0, 0, 0))

            elif type == 'T5':
                img = Image.open('./cert_files/frame/T5-1.jpg')
                I1 = ImageDraw.Draw(img)
                _, _, w1, h1 = I1.textbbox((0, 0), name, font=font30)
                I1.text((l+round((w-l-w1)/2), 520), name, font=font30, fill =(0, 0, 0))

                ptext = project.split('\n')
                if len(ptext) > 0:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[0], font=font24)
                    I1.text((l+round((w-l-w2)/2), 800), ptext[0], font=font24, fill =(0, 0, 0))
                if len(ptext) > 1:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[1], font=font24)
                    I1.text((l+round((w-l-w2)/2), 840), ptext[1], font=font24, fill =(0, 0, 0))
                if len(ptext) > 2:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[2], font=font24)
                    I1.text((l+round((w-l-w2)/2), 880), ptext[2], font=font24, fill =(0, 0, 0))

            elif type == 'T10':
                img = Image.open('./cert_files/frame/T10-1.jpg')
                I1 = ImageDraw.Draw(img)
                _, _, w1, h1 = I1.textbbox((0, 0), name, font=font30)
                I1.text((l+round((w-l-w1)/2), 520), name, font=font30, fill =(0, 0, 0))

                ptext = project.split('\n')
                if len(ptext) > 0:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[0], font=font24)
                    I1.text((l+round((w-l-w2)/2), 800), ptext[0], font=font24, fill =(0, 0, 0))
                if len(ptext) > 1:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[1], font=font24)
                    I1.text((l+round((w-l-w2)/2), 840), ptext[1], font=font24, fill =(0, 0, 0))
                if len(ptext) > 2:
                    _, _, w2, h2 = I1.textbbox((0, 0), ptext[2], font=font24)
                    I1.text((l+round((w-l-w2)/2), 880), ptext[2], font=font24, fill =(0, 0, 0))

            elif type == 'TA':
                img = Image.open('./cert_files/frame/TA-1.jpg')
                I1 = ImageDraw.Draw(img)
                _, _, w1, h1 = I1.textbbox((0, 0), name, font=font30)
                I1.text((l+round((w-l-w1)/2), 560), name, font=font30, fill =(0, 0, 0))

            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=75)
            # img.save(buffer, format='PNG')

            imgb64 = base64.b64encode(buffer.getvalue())
            # rv = rv.decode('ascii')

            # Display edited image
            img.show()

            # Save the edited image
            # img.save("img.jpg")

            image = 'data:image/jpeg;base64,' + str(imgb64)

        return { 'status': 0, 'image': image }, 200


api.add_resource(GenCert, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
