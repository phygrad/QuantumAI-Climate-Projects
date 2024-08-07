Project 2: Fast-Running AI Model of the Earth’s Climate
a) Problem Statement and Background

Problem Statement:
Climate models are essential for understanding the interactions between the Earth's climate and its ecosystems. Traditional climate models are computationally expensive, often requiring supercomputing resources to run detailed simulations. This project aims to develop a fast-running AI model of the Earth's climate that can operate on a standard laptop or PC, providing accessible and efficient climate predictions.

Background:
Understanding and predicting climate change is crucial for mitigating its impacts on human activities and natural ecosystems. Traditional climate models involve solving complex physical equations, which is time-consuming and resource-intensive. By developing an AI-based climate model, we can make climate predictions more accessible and quicker, aiding in timely decision-making and policy formulation.
b) Background Research and Literature Review

Literature Review:

    Traditional Climate Models:
        Climate models simulate the interactions of the atmosphere, oceans, land surface, and ice. These models solve physical equations based on fluid dynamics, thermodynamics, and radiation.
        Reference: IPCC. (2013). Climate Change 2013: The Physical Science Basis.

    AI in Climate Modeling:
        AI, particularly deep learning models, has been used to approximate climate processes, reducing the need for computationally intensive simulations.
        Reference: Reichstein, M., Camps-Valls, G., Stevens, B., Jung, M., Denzler, J., Carvalhais, N., & Prabhat. (2019). Deep learning and process understanding for data-driven Earth system science. Nature, 566(7743), 195-204.

    Advantages and Disadvantages:
        Traditional models are highly accurate but require significant computational resources.
        AI models can run faster and on less powerful hardware but may struggle with capturing complex interactions and long-term trends.

c) AI Methods for Climate Modeling

AI Methods:

    Recurrent Neural Networks (RNNs):
        Use RNNs, such as Long Short-Term Memory (LSTM) networks, to model temporal climate data, capturing patterns and trends over time.
        Algorithm: LSTM networks are suitable for time-series prediction due to their ability to remember long-term dependencies.

    Generative Adversarial Networks (GANs):
        Employ GANs to generate high-resolution climate data from coarse input data, improving the spatial resolution of predictions.
        Algorithm: GANs consist of a generator and a discriminator network that compete against each other, improving the quality of generated data.

Results and Computational Resources:

    AI Results: LSTM models accurately predict short-term climate variables with significantly reduced computation times. GANs enhance the resolution of climate data, making detailed predictions possible on standard hardware.

Advantages of AI Methods:

    AI models provide fast and efficient climate predictions, making them accessible on standard laptops or PCs.
    They offer the potential for real-time updates and fine-tuned local climate forecasts.


### Files
- `code/ai_model.py`: AI model training and prediction code.
- `code/data_preprocessing.py`: Data preprocessing script.
- `data/historical_climate_data.csv`: Preprocessed historical climate data.

### Instructions
1. Run `data_preprocessing.py` to preprocess raw data.
2. Run `ai_model.py` to train the model and make predictions.
3. Ensure `historical_climate_data.csv` is in the data folder.
