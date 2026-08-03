"""
=========================================================
Analytics Service
AI Powered Car Price Prediction System
=========================================================

This service performs all dataset analysis required by

✔ Dashboard
✔ EDA
✔ Model Performance
✔ AI Insights

Never calculate statistics directly inside pages.
Always use this service.

=========================================================
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class AnalyticsService:

    # =====================================================
    # DATASET SUMMARY
    # =====================================================

    @staticmethod
    def dataset_summary(df):

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "duplicates": int(df.duplicated().sum()),

            "missing": int(df.isnull().sum().sum())

        }

    # =====================================================
    # PRICE SUMMARY
    # =====================================================

    @staticmethod
    def price_summary(df):

        return {

            "min": float(df["Price"].min()),

            "max": float(df["Price"].max()),

            "mean": float(df["Price"].mean()),

            "median": float(df["Price"].median()),

            "std": float(df["Price"].std())

        }

    # =====================================================
    # COMPANY STATS
    # =====================================================

    @staticmethod
    def company_statistics(df):

        return (

            df.groupby("company")

            .agg(

                Cars=("company","count"),

                AveragePrice=("Price","mean"),

                AverageKM=("kms_driven","mean")

            )

            .sort_values(

                by="Cars",

                ascending=False

            )

        )

    # =====================================================
    # FUEL STATS
    # =====================================================

    @staticmethod
    def fuel_statistics(df):

        return (

            df["fuel_type"]

            .value_counts()

        )

    # =====================================================
    # YEAR STATS
    # =====================================================

    @staticmethod
    def year_statistics(df):

        return (

            df.groupby("year")

            .size()

        )

    # =====================================================
    # CORRELATION
    # =====================================================

    @staticmethod
    def correlation(df):

        numeric = df.select_dtypes(

            include=np.number

        )

        return numeric.corr()

    # =====================================================
    # MISSING VALUES
    # =====================================================

    @staticmethod
    def missing_values(df):

        return (

            df.isnull()

            .sum()

            .sort_values(

                ascending=False

            )

        )

    # =====================================================
    # OUTLIERS
    # =====================================================

    @staticmethod
    def outliers(

        df,

        column

    ):

        q1 = df[column].quantile(.25)

        q3 = df[column].quantile(.75)

        iqr = q3-q1

        lower = q1-1.5*iqr

        upper = q3+1.5*iqr

        return df[

            (df[column]<lower)

            |

            (df[column]>upper)

        ]

    # =====================================================
    # TOP BRANDS
    # =====================================================

    @staticmethod
    def top_brands(

        df,

        top=10

    ):

        return (

            df["company"]

            .value_counts()

            .head(top)

        )

    # =====================================================
    # TOP EXPENSIVE BRANDS
    # =====================================================

    @staticmethod
    def premium_brands(df):

        return (

            df.groupby("company")["Price"]

            .mean()

            .sort_values(

                ascending=False

            )

            .head(10)

        )

    # =====================================================
    # CHEAPEST BRANDS
    # =====================================================

    @staticmethod
    def cheapest_brands(df):

        return (

            df.groupby("company")["Price"]

            .mean()

            .sort_values()

            .head(10)

        )

    # =====================================================
    # FEATURE SUMMARY
    # =====================================================

    @staticmethod
    def describe(df):

        return df.describe(
            include="all"
        )


    # =====================================================
    # PRICE BY FUEL
    # =====================================================

    @staticmethod
    def average_price_by_fuel(df):

        return (

            df.groupby(

                "fuel_type"

            )["Price"]

            .mean()

        )

    # =====================================================
    # PRICE BY YEAR
    # =====================================================

    @staticmethod
    def average_price_by_year(df):

        return (

            df.groupby(

                "year"

            )["Price"]

            .mean()

        )

    # =====================================================
    # KMS SUMMARY
    # =====================================================

    @staticmethod
    def kms_statistics(df):

        return {

            "min": df["kms_driven"].min(),

            "max": df["kms_driven"].max(),

            "mean": df["kms_driven"].mean(),

            "median": df["kms_driven"].median()

        }


analytics_service = AnalyticsService()

