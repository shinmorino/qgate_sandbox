#define _USE_MATH_DEFINES  /* to define M_PI on Windows. */
#include <math.h>
#include "GateMatrix.h"

using namespace qgate;

namespace {

std::complex<double> j(0., 1.);

}

void qgate::U_mat(Matrix2x2C64 &mat, double theta, double phi, double lambda) {
    double theta2 = theta * 0.5;
    double cos_theta_2 = std::cos(theta2);
    double sin_theta_2 = std::sin(theta2);

    /* Ref: https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=002-The_Weird_and_Wonderful_World_of_the_Qubit~2F004-advanced_qubit_gates */
    mat(0, 0) =                                  cos_theta_2;
    mat(0, 1) = - std::exp(j * lambda)         * sin_theta_2;
    mat(1, 0) =   std::exp(j * phi)            * sin_theta_2;
    mat(1, 1) =   std::exp(j * (lambda + phi)) * cos_theta_2;
}

void qgate::U2_mat(Matrix2x2C64 &mat, double phi, double lambda) {
    mat(0, 0) =   1.;
    mat(0, 1) = - std::exp(j * lambda);
    mat(1, 0) =   std::exp(j * phi);
    mat(1, 1) =   std::exp(j * (lambda + phi));
}

void qgate::U1_mat(Matrix2x2C64 &mat, double lambda) {
    mat(0, 0) =   1.;
    mat(0, 1) =   0.;
    mat(1, 0) =   0.;
    mat(1, 1) =   std::exp(j * lambda);
}

void qgate::ID_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   1.;
    mat(0, 1) =   0.;
    mat(1, 0) =   0.;
    mat(1, 1) =   1.;
}

void qgate::X_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   0.;
    mat(0, 1) =   1.;
    mat(1, 0) =   1.;
    mat(1, 1) =   0.;
}

void qgate::Y_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   0.;
    mat(0, 1) = - j;
    mat(1, 0) =   j;
    mat(1, 1) =   0.;
}

void qgate::Z_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   1.;
    mat(0, 1) =   0.;
    mat(1, 0) =   0.;
    mat(1, 1) = - 1.;
}

void qgate::H_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   1. * std::sqrt(0.5);
    mat(0, 1) =   1. * std::sqrt(0.5);
    mat(1, 0) =   1. * std::sqrt(0.5);
    mat(1, 1) = - 1. * std::sqrt(0.5);
}

void qgate::S_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   1.;
    mat(0, 1) =   0.;
    mat(1, 0) =   0.;
    mat(1, 1) =   j;
}

void qgate::T_mat(Matrix2x2C64 &mat) {
    mat(0, 0) =   1.;
    mat(0, 1) =   0.;
    mat(1, 0) =   0.;
    mat(1, 1) =   std::exp(M_PI * 0.25 * j);
}

void qgate::RX_mat(Matrix2x2C64 &mat, double theta) {
    double theta2 = theta / 2.;
    double cos_theta_2 = std::cos(theta2);
    double sin_theta_2 = std::sin(theta2);
    mat(0, 0) =       cos_theta_2;
    mat(0, 1) = - j * sin_theta_2;
    mat(1, 0) = - j * sin_theta_2;
    mat(1, 1) =       cos_theta_2;
}

void qgate::RY_mat(Matrix2x2C64 &mat, double theta) {
    double theta2 = theta / 2.;
    double cos_theta_2 = std::cos(theta2);
    double sin_theta_2 = std::sin(theta2);
    mat(0, 0) =   cos_theta_2;
    mat(0, 1) = - sin_theta_2;
    mat(1, 0) =   sin_theta_2;
    mat(1, 1) =   cos_theta_2;
}

void qgate::adjoint(Matrix2x2C64 *_mat) {
    Matrix2x2C64 &mat = *_mat;
    mat(0, 0) = std::conj(mat(0, 0));
    qgate::ComplexType<double> tmp = mat(0, 1);
    mat(0, 1) = std::conj(mat(1, 0));
    mat(1, 0) = std::conj(tmp);
    mat(1, 1) = std::conj(mat(1, 1));
}
