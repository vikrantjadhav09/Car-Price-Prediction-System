"""
=========================================================
Dataset Service
=========================================================
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT / "Data" / "cleaned_car_data.csv"


class DatasetService:

    @staticmethod
    @st.cache_data
    def load():

        return pd.read_csv(DATA_PATH)

    @staticmethod
    def summary(df):

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "brands": df["company"].nunique(),

            "fuel_types": df["fuel_type"].nunique(),

            "min_year": int(df["year"].min()),

            "max_year": int(df["year"].max())

        }

    @staticmethod
    def average_price(df):

        return float(df["Price"].mean())

    @staticmethod
    def max_price(df):

        return float(df["Price"].max())

    @staticmethod
    def min_price(df):

        return float(df["Price"].min())

    @staticmethod
    def companies(df):

        return sorted(df["company"].unique())

    @staticmethod
    def fuel_types(df):

        return sorted(df["fuel_type"].dropna().unique())

    @staticmethod
    def years(df):

        return sorted(df["year"].unique())

    @staticmethod
    def filter(

        df,

        company=None,

        fuel=None,

        year=None,

    ):

        result = df.copy()

        if company and company != "All":

            result = result[result["company"] == company]

        if fuel and fuel != "All":

            result = result[result["fuel_type"] == fuel]

        if year:

            result = result[result["year"] == year]

        return result

    @staticmethod
    def search(df, text):

        if not text:

            return df

        mask = df.astype(str).apply(

            lambda row:

            row.str.contains(

                text,

                case=False

            ).any(),

            axis=1,

        )

        return df[mask]


    @staticmethod
    def top_brands(df, top=10):

        return (

            df["company"]

            .value_counts()

            .head(top)

        )

    @staticmethod
    def latest(df, n=10):

        return df.tail(n)

    @staticmethod
    def sample(df, n=5):

        return df.sample(n)

    @staticmethod
    def price_statistics(df):

        return {

            "mean": float(df["Price"].mean()),

            "median": float(df["Price"].median()),

            "min": float(df["Price"].min()),

            "max": float(df["Price"].max())

        }


dataset_service = DatasetService()




