{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2a120b9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pick an option between R, P, S : S\n",
      "Player (S) : CPU (S)\n",
      "It's a tie!\n",
      "Play again? (y/n): R\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "while True:\n",
    "    user_option = input(\"Pick an option between R, P, S : \")\n",
    "    possible_options = [\"R\", \"P\", \"S\"]\n",
    "    while user_option not in possible_options:\n",
    "        print(\"Error!...invalid option!\")\n",
    "        input(\"Please pick another option between R, P, S : \")\n",
    "\n",
    "    computer_option = random.choice(possible_options)\n",
    "    print(\"Player ({}) : CPU ({})\".format(user_option, computer_option))\n",
    "\n",
    "    if user_option == \"R\" and computer_option == \"S\":\n",
    "        print(\"Rock beats scissors! You win!\")\n",
    "    elif user_option == \"P\" and computer_option == \"R\":\n",
    "        print(\"Paper beats rock! You win!\")\n",
    "    elif user_option == \"S\" and computer_option == \"P\":\n",
    "        print(\"Scissors beats paper! You win!\")\n",
    "    elif user_option == computer_option:\n",
    "        print(\"It's a tie!\")\n",
    "        play_again = input(\"Play again? (y/n): \")\n",
    "        if play_again.lower() != \"y\":\n",
    "            break\n",
    "    else:\n",
    "        print(\"CPU win! You lose.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "678a3e55",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
