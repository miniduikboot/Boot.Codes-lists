# Boot.Codes Lists

This is a set of game codes for [Boot.Codes](https://github.com/miniduikboot/Boot.Codes), which is an Impostor plugin that sets your Room Code to something that's easier to shout down a microphone.

This is a word list based on research from the University of Ghent[1] which measured word prevalence of 61,800 words in the English language. This script takes a CSV converted version of their data, filters on word length and removes bad words, both from a predefined bad words list, as well as manually removed words from the output.

The prevalence of a word indicates how common it is in use:

- 2.0: 98% of people know this word
- 2.5: nearly everyone that took part in this researchknows this word

Word lists with a lower prevalence are longer, but may contain words you're less familiar with. You can find the [lists](lists) in this repository.

Currently we only created lists with a prevalence of 2.0 or higher for a word size of 6, but more may be produced in future.

# Policy on removing words

We're very lenient on removing words: we don't want a bad room code ruining someones game experience. There are enough words in the list that removing a few words does not reduce the quality of the list. While we've checked the list manually, there may still be words in there that may cause a bad experience.

If you notice a word that you feel shouldn't be there, feel free to open an issue here or contact miniduikboot#2965 in the Impostor Discord.

# License

This list is derived from Brysbaert et al[1]. They have provided their data under the CC-BY-NC-SA 4.0 license, which we'll follow as well.

[1]: Brysbaert, M., Mandera, P., McCormick, S.F., & Keuleers, E. (2019). Word prevalence norms for 62,000 English lemmas. Behavior Research Methods, 51(2), 467-479. http://crr.ugent.be/archives/2045
