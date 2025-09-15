{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e9256861-bbd1-4382-adb5-f3e5cad287ae",
   "metadata": {},
   "source": [
    "PROBLEM 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3db1a009-455d-42e1-91be-5c74d8574c4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "72a67bde-37f5-422e-baca-9d2592203ade",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 5 rows, odd-numbered columns\n",
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n",
      "\n",
      " Row for Model == 'Mazda RX4'\n",
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n",
      "\n",
      " Cylinders of 'Camaro Z28'\n",
      "         Model  cyl\n",
      "23  Camaro Z28    8\n",
      "\n",
      " cyl and gear for selected models\n",
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "cars = pd.read_csv(\"http://bit.ly/Cars_file\")\n",
    "\n",
    "# a) First five rows with odd-numbered columns (1-indexed: 1,3,5,7…)\n",
    "#In pandas (0-indexed), that is columns 0,2,4,6… via iloc and step 2.\n",
    "print(\"First 5 rows, odd-numbered columns\")\n",
    "print(cars.iloc[:5, ::2])\n",
    "\n",
    "# b)Row that contains Model == Mazda RX4 (label selection)\n",
    "print(\"\\n Row for Model == 'Mazda RX4'\")\n",
    "print(cars.loc[cars[\"Model\"] == \"Mazda RX4\"])\n",
    "\n",
    "# c) Cylinders of Camaro Z28\n",
    "print(\"\\n Cylinders of 'Camaro Z28'\")\n",
    "print(cars.loc[cars[\"Model\"] == \"Camaro Z28\", [\"Model\", \"cyl\"]])\n",
    "\n",
    "# d) cyl and gear for Mazda RX4 Wag, Ford Pantera L, Honda Civic\n",
    "print(\"\\n cyl and gear for selected models\")\n",
    "sel = (cars[\"Model\"] == \"Mazda RX4 Wag\") | (cars[\"Model\"] == \"Ford Pantera L\") | (cars[\"Model\"] == \"Honda Civic\")\n",
    "print(cars.loc[sel, [\"Model\", \"cyl\", \"gear\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6b101b9-5c48-4b38-a317-4b4c7d055135",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
