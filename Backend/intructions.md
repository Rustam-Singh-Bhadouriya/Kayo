# Kayo Virtual Asistent Backend

### upgrades and fixes - 
- *Offline and qualited Speech-To-Text*
- *two model support! (Need Some More Tests)*
- *User Simplexity*
- *Every Language Support (need some setup explained in ahead)*

________________

## Explainations -
### *Offline and qualited Speech-To-Text*
<p>
The Speech-To-Text is build with vosk a offline module with every language Support

Download Model <a href="https://alphacephei.com/vosk/models">Vosk Model Official Site</a>

*and paste your model's path at `voices.py`*

```bash
model = Model(r"YOUR_MODEL_PATH")
```
</p>

### *two model support!*
<p>

*On Testing Release Soon With DeepSeek and Gemini Support!*

</p>



### *User Simplexity*
<p>

Just run `build.py` after installing Python!
<br>

#### Some Setups You Need
- *Setup API*
    <br>
    ***to get gemini api visit and get you API***
    <a href="https://www.studio.google.com">Gemini Dashboard</a>
    <br>

    *Place you API at `api.py`*
    ```bash
    api_gemini = "GEMINI_API_KEY"
    ```

- *Setup Modules*
    <br>
    To Install Modules Just Run `build.py`
</p>

#### Every Language Support
<p>
To get all language support just download any model from <a href="https://alphacephei.com/vosk/models">Vosk Model Official Site</a>

*and paste your model's path at `voices.py`*

```bash
model = Model(r"YOUR_MODEL_PATH")
```
</p>



## Contribute
**You Can Colaburate with**
- Creating issues
- pulling requests

***Thank You!***