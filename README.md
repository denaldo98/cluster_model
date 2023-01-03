# cluster_model

Package containing a wrapper class <i>River</i> for performinc Online Topic Modeling with BERTopic model as explained in the [related documentation](https://maartengr.github.io/BERTopic/getting_started/online/online.html).

The reference documentation states that the package [river](https://riverml.xyz/0.14.0/) can be used for performing Online Topic Modeling. However it is necessary to create a class having a `.partial_fit` function and the possibility to extract labels through `.labels`.

The module simply defines a Python class `class River` as specified in the BERTopic guidelines for performing Online Topic Modeling with a clutering model taken from [river](https://riverml.xyz/0.14.0/), which allows to instantiate a cluster model taken from [river](https://riverml.xyz/0.14.0/), adding the `.partial_fit` function and the possibility to extract labels through `.labels`.
