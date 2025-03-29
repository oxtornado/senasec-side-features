## senasec - facial recognition  classroom opening system 
## Authors

- [@oxtornado](https://www.github.com/oxtornado)


---
This is a side project, where i will be testing libraries who accomplish the general objective; a facial recognition web who also implements Arduino for showing how after you enter the classroom, the classroom opens to you. Poetic, ik.

This is going to be a step by step guide and documentating all the error it may occur, w nothing else to say, follow along this journey!


## Journey - Documentation

### Fri, Mar 28.
Aw god, idk where to start. Actually, I do.
1. I simply search for 'ai facial recognition api free' at Google, this took me to [Eden AI](https://www.edenai.co/), cool web tho, where I understand it id for AI API integration (?) anyway, this took me to nowhere, but at least look for more tools that my dev junior brain that understand basic concepts of CS did not understand at all. 

Then, going thu the results of my latest Google search I found [Imagga](https://imagga.com/) which you can not tell it's not made by Django. Made and account and got my API Token (please imagine the scene in Gravity Falls where Dipper screams when the real Stan says 'that's when I started the diaries'). Buut, what should doechii do, i was so confuseeedd. So, as a dev with brain rot, I looked for help, AI help, great help. 

I knew chat-gpt not always can scan web-pages, so i keep thinking and thougt of [Google Notebooks](https://notebooklm.google/) which are cool because, they only work with the information you bring them, information that can be the Imagga's documentation (God I love you make me born in the AI era) anyway. I passed the documentation link and told it what I had in mind and if Imagga could help with it and basically said 'yeah, sure, but like, you know API REST, right?' API? REST? Kidding, I do know, a little, but I'm familiar with concepts like tokens, permissions, roles or endpoints.

After knowing this tool was a real alternative I went to my AI best-friend, Mr Chat-GPT, my beloved.

Pass the prompt "tengo un proyecto en mente, senasec, este proyecto, de manera local, usando la api Imagga, reconoce rostros de personas especificas, si la reconoce, activa un servomotor, para que se mueva, de modo que se vea como si se abriera una puerta. Es un sistema de apertura de salones por reconocimiento facial. Podrias ayudarme a construirlo". Although I know it may not be the best prompt, it helped me to divide the project in little tasks to achieve and only I know tonight it's the night (Bubblegum electric by Gwen Stefani starts playing).

---

#### 📈 Progreso en el Proyecto SENASEC

Durante esta sesión, avanzamos significativamente en el desarrollo del sistema de reconocimiento facial para la apertura de puertas.

  1. Integración con la API de Imagga
  - Se probó la API con una imagen de referencia y se confirmó que detecta rostros correctamente.

  2. Creación de la base de datos de usuarios
  - Se implementó un sistema para almacenar imágenes de usuarios autorizados.
  - Se agregaron los primeros usuarios a la base de datos.


  3. Implementación del reconocimiento facial con DeepFace
  - Se compararon imágenes en tiempo real con las fotos almacenadas.
  - Se ajustó el modelo de reconocimiento a **Facenet512** para mayor precisión.
  - Se configuró un umbral más estricto para evitar falsos positivos.
  - Se realizaron pruebas con imágenes reales y se confirmó que el sistema distingue correctamente entre usuarios autorizados y no autorizados.

#### 🛠 Próximos pasos:
- Integrar Arduino y un servomotor para que la "puerta" se abra cuando se verifique la identidad.