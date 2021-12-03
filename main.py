from sklearn.datasets import load_breast_cancer
from sklearn.compose import Pipeline
from sklearn.covariance import EmpiricalCovariance, MinCovDet
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def main():
    dataset = load_breast_cancer()


if __name__ == "__main__":
    main()
